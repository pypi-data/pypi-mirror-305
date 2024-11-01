from importlib import metadata as _metadata

from s3pro.entities import (  # noqa: F401
    S3,
    Bucket,
    Object,
)

try:
    __version__ = _metadata.version('r3pro')

except _metadata.PackageNotFoundError:
    __version__ = '0.0.0'
