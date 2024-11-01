from uuid import uuid4

from s3pro import S3, Object


class TestS3(object):
    async def test_get_buckets(self, s3: S3):
        await s3.get_buckets()

    async def test_create_bucket(self, s3: S3):
        bucket_uuid = str(uuid4())
        bucket = await s3.create_bucket(bucket_uuid)
        assert bucket.name == bucket_uuid

    async def test_delete_bucket(self, s3: S3):
        bucket_uuid = str(uuid4())
        bucket = await s3.create_bucket(bucket_uuid)
        await bucket.delete()


class TestBucket:
    async def test_get_buckets(self, s3: S3):
        await s3.get_buckets()


class TestObject:
    async def test_upload_data(self, s3_object: Object):
        await s3_object.upload(b'test')

    async def test_link(self, s3_object: Object):
        assert await s3_object.share()
