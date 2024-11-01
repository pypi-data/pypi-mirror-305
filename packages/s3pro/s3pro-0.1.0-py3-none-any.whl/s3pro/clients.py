from __future__ import annotations

import asyncio
import json
from collections.abc import AsyncIterator
from datetime import datetime
from io import BytesIO
from typing import Any, BinaryIO
from xml.etree import ElementTree

import httpx
from httpx import Response

from s3pro.auth import AwsSigV4
from s3pro.exceptions import S3Exception
from s3pro.utils import NS_URL, get_xml_attr

IGNORED_ERRORS = {'BucketAlreadyOwnedByYou'}

LAST_MODIFIED_DATETIME_FORMAT = '%a, %d %b %Y %H:%M:%S %Z'


MULTIPART_THRESHOLD: int = 16 * 1024 * 1024
MAX_CONCURRENCY: int = 6


class Client(object):
    def __init__(
        self,
        endpoint: str | None = None,
        aws_access_key_id: str | None = None,
        aws_secret_access_key: str | None = None,
        region: str | None = None,
        singer: AwsSigV4 | None = None,
    ):
        self._endpoint = endpoint

        if singer is None:
            assert all([aws_access_key_id, aws_secret_access_key])
            singer = AwsSigV4(
                aws_access_key_id,
                aws_secret_access_key,
                region,
            )

        self.signer = singer
        self.session = httpx.AsyncClient()

    @staticmethod
    def raise_error(response: Response) -> None:
        if response.status_code < 400:
            return

        try:
            error = ElementTree.parse(BytesIO(response.text.encode('utf8'))).getroot()

        except Exception as e:
            raise S3Exception('S3Error', 'Failed to parse response xml.') from e

        error_code = get_xml_attr(error, 'Code', ns='').text
        error_message = get_xml_attr(error, 'Message', ns='').text

        if error_code not in IGNORED_ERRORS:
            raise S3Exception(error_code, error_message)

    async def _upload_object_multipart(self, bucket: str, key: str, file: BinaryIO) -> Object | None:
        key = key.lstrip('/')

        # Create multipart upload
        resp = await self.post(f'{self._endpoint}/{bucket}/{key}?uploads=')
        self.raise_error(resp)
        res = ElementTree.parse(BytesIO(resp.text.encode('utf8'))).getroot()
        upload_id = get_xml_attr(res, 'UploadId').text

        sem = asyncio.Semaphore(MAX_CONCURRENCY)

        async def _upload_task(part_number: int, content: bytes):
            await sem.acquire()

            url = f'{self._endpoint}/{bucket}/{key}?partNumber={part_number}&uploadId={upload_id}'
            resp_ = await self.put(url, content=content, headers={})
            self.raise_error(resp_)
            etag = resp_.headers['ETag']

            sem.release()
            return part_number, f'<Part><ETag>{etag}</ETag><PartNumber>{part_number}</PartNumber></Part>'

        # Upload parts
        part = 1
        total_size = 0
        tasks = []
        while data := file.read(MULTIPART_THRESHOLD):
            total_size += len(data)
            tasks.append(asyncio.create_task(_upload_task(part, data)))
            part += 1

        parts = sorted(await asyncio.gather(*tasks))
        parts = ''.join([part[1] for part in parts])

        # Complete upload
        body = (
            f'<?xml version="1.0" encoding="UTF-8"?>'
            f'<CompleteMultipartUpload xmlns="{NS_URL}">{parts}</CompleteMultipartUpload>'
        ).encode()
        resp = await self.post(f'{self._endpoint}/{bucket}/{key}?uploadId={upload_id}', content=body)
        self.raise_error(resp)

        return Object(Bucket(bucket, client=self), key, datetime.now(), total_size, client=self)

    #
    #
    #
    #
    #
    #
    #

    async def head(
        self,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        headers: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> Response:
        headers = self.signer.sign(url, headers, 'HEAD', add_signature=True, params=params)
        return await self.session.head(url=url, headers=headers, params=params, **kwargs)

    async def get(
        self,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        headers: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> Response:
        headers = self.signer.sign(url, headers, add_signature=True, params=params)
        return await self.session.get(url=url, headers=headers, params=params, **kwargs)

    async def put(
        self,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        content: bytes | None = None,
        headers: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> Response:
        headers = self.signer.sign(url, headers, 'PUT', content or b'', add_signature=True, params=params)
        return await self.session.put(url=url, content=content, headers=headers, params=params, **kwargs)

    async def post(
        self,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        content: bytes | None = None,
        headers: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> Response:
        headers = self.signer.sign(url, headers, 'POST', content or b'', add_signature=True, params=params)
        return await self.session.post(url=url, content=content, headers=headers, params=params, **kwargs)

    async def delete(
        self,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        headers: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> Response:
        headers = self.signer.sign(url, headers, 'DELETE', add_signature=True, params=params)
        return await self.session.delete(url=url, headers=headers, params=params, **kwargs)

    #
    #
    #
    #
    #
    #
    #
    #
    #

    async def delete_bucket(self, bucket_name: str) -> None:
        resp = await self.delete(f'{self._endpoint}/{bucket_name}/')
        self.raise_error(resp)

    async def get_buckets_names(self) -> list[str]:
        buckets: list[str] = []

        resp = await self.get(f'{self._endpoint}/')
        self.raise_error(resp)
        res = ElementTree.parse(BytesIO(resp.text.encode('utf8'))).getroot()

        for obj in get_xml_attr(res, 'Bucket', True):
            name = get_xml_attr(obj, 'Name').text

            buckets.append(name)

        return buckets

    async def create_bucket(self, bucket_name: str) -> str:
        body = (
            f'<?xml version="1.0" encoding="UTF-8"?>'
            f'<CreateBucketConfiguration xmlns="{NS_URL}"></CreateBucketConfiguration>'
        ).encode()

        resp = await self.put(f'{self._endpoint}/{bucket_name}', content=body)
        self.raise_error(resp)

        return bucket_name

    #
    #
    #
    #
    #

    async def get_object(self, bucket_name: str, object_name: str) -> tuple[str, datetime | None, int] | None:
        object_name = object_name.lstrip('/')

        resp = await self.head(f'{self._endpoint}/{bucket_name}/{object_name}')

        if resp.status_code != 200:
            return

        updated_at = datetime.fromisoformat(resp.headers['Last-Modified']) if 'Last-Modified' else None
        size = int(resp.headers['Content-Length'])

        return object_name, updated_at, size

    async def delete_object(self, bucket_name: str, object_name: str) -> tuple[str, datetime | None, int] | None:
        object_name = object_name.lstrip('/')
        resp = await self.delete(f'{self._endpoint}/{bucket_name}/{object_name}')
        self.raise_error(resp)

    async def get_objects(
        self,
        bucket_name: str,
        prefix: str | None = None,
        max_keys: int | None = None,
    ) -> AsyncIterator[tuple[str, datetime | None, int]]:
        more_objects = True
        marker = None
        got_objects = 0

        while more_objects and (max_keys is None or got_objects < max_keys):
            params = {}
            if prefix is not None:
                params['prefix'] = prefix
            if max_keys is not None:
                params['max-keys'] = min(max_keys - got_objects, 1000)
            if marker is not None:
                params['marker'] = marker

            resp = await self.get(f'{self._endpoint}/{bucket_name}', params=params)
            self.raise_error(resp)
            res = ElementTree.parse(BytesIO(resp.text.encode('utf8'))).getroot()

            more_objects = get_xml_attr(res, 'IsTruncated').text.lower() == 'true'

            for obj in get_xml_attr(res, 'Contents', True):
                got_objects += 1
                name = marker = get_xml_attr(obj, 'Key').text
                updated_at = datetime.fromisoformat(get_xml_attr(obj, 'LastModified').text)
                size = int(get_xml_attr(obj, 'Size').text)

                yield (name, updated_at, size)

    #
    #
    #
    #
    #

    async def get_bucket_policy(self, bucket_name: str) -> dict[str, Any]:
        resp = await self.get(f'{self._endpoint}/{bucket_name}/?policy=')
        self.raise_error(resp)
        return resp.json()

    async def put_bucket_policy(self, bucket_name: str, policy: dict[str, Any]) -> None:
        policy_bytes = json.dumps(policy).encode('utf8')

        resp = await self.put(f'{self._endpoint}/{bucket_name}/?policy=', content=policy_bytes)
        self.raise_error(resp)

    async def delete_bucket_policy(self, bucket_name: str) -> None:
        resp = await self.delete(f'{self._endpoint}/{bucket_name}/?policy=')
        self.raise_error(resp)

    #
    #
    #
    #
    #

    async def share(self, bucket_name: str, key: str, ttl: int = 86400, upload: bool = False) -> str:
        key = key.lstrip('/')
        return self.signer.presign(f'{self._endpoint}/{bucket_name}/{key}', upload, ttl)

    #
    #
    #
    #

    async def download_object(
        self,
        bucket_name: str,
        object_name: str,
        offset: int = 0,
        limit: int = 0,
    ) -> BytesIO:
        object_name = object_name.lstrip('/')

        if object_name.startswith('/'):
            object_name = object_name[1:]

        headers: dict[str, Any] = {}

        if offset > 0 or limit > 0:
            offset = max(offset, 0)
            limit = max(limit, 0)
            headers['Range'] = f'bytes={offset}-{offset + limit - 1}' if limit else f'bytes={offset}-'

        resp = await self.get(f'{self._endpoint}/{bucket_name}/{object_name}', headers=headers)
        self.raise_error(resp)
        content = await resp.aread()

        return BytesIO(content)

    async def upload_object(self, bucket_name: str, object_name: str, content: bytes) -> tuple[str, datetime, int]:
        object_name = object_name.lstrip('/')

        size = len(content)
        # if file_size > MULTIPART_THRESHOLD:
        #     return await self._upload_object_multipart(bucket_name, object_name, content)

        resp = await self.put(f'{self._endpoint}/{bucket_name}/{object_name}', content=content)
        self.raise_error(resp)

        return object_name, datetime.now(), size
