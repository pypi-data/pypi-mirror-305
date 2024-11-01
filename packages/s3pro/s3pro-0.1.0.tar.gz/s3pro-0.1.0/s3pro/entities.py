from __future__ import annotations

from collections.abc import Sequence
from datetime import datetime

from s3pro.auth import AwsSigV4
from s3pro.clients import Client


class S3(object):
    def __init__(
        self,
        endpoint: str | None = None,
        aws_access_key_id: str | None = None,
        aws_secret_access_key: str | None = None,
        region: str | None = None,
        client: Client | None = None,
        singer: AwsSigV4 | None = None,
    ) -> None:
        if client is None:
            client = Client(
                endpoint,
                aws_access_key_id,
                aws_secret_access_key,
                region,
                singer,
            )

        self.client = client

    async def get_bucket(self, bucket_name: str) -> Bucket:
        return Bucket(bucket_name, client=self.client)

    async def get_buckets(self) -> Sequence[Bucket]:
        return [Bucket(i, client=self.client) for i in await self.client.get_buckets_names()]

    async def create_bucket(self, bucket_name: str) -> Bucket:
        await self.client.create_bucket(bucket_name)
        return Bucket(bucket_name, client=self.client)


class Bucket(object):
    def __init__(self, name: str, *, client: Client):
        self.name = name
        self.client = client

    def __repr__(self) -> str:  # pragma: no cover
        return f'Bucket(name={self.name!r})'

    async def get_objects(self):
        objs: list[Object] = []

        async for name, updated_at, size in self.client.get_objects(self.name):
            objs.append(Object(self, name, updated_at, size, client=self.client))

        return objs

    async def delete(self):
        await self.client.delete_bucket(self.name)

    async def create_object(self, object_name: str, content: bytes):
        data = await self.client.upload_object(self.name, object_name, content)
        return Object(self, *data, client=self.client)


class Object(object):
    def __init__(self, bucket: Bucket, name: str, last_modified: datetime | None, size: int, *, client: Client):
        self.bucket = bucket
        self.name = name
        self.last_modified = last_modified
        self.size = size
        self.client = client

    def __repr__(self) -> str:  # pragma: no cover
        return f'Object(bucket={self.bucket!r}, name={self.name!r}, size={self.size!r})'

    async def upload(self, content: str | bytes):
        await self.client.upload_object(self.bucket.name, self.name, content)

    async def delete(self):
        await self.client.delete_object(self.bucket.name, self.name)

    async def share(self):
        return await self.client.share(self.bucket.name, self.name)
