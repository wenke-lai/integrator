import pulumi
from pulumi_aws import get_arn, s3

from diagrams.eraser import cloud_architecture as diagram

from .object import Object


class Bucket(s3.BucketV2):
    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new S3 Bucket.

        Args:
            resource_name (str): The name of the S3 Bucket.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/s3/bucketv2/#inputs)
        """

        super().__init__(resource_name, **kwargs)

        self.diagram = diagram.Node(resource_name, icon="aws-simple-storage-service")

    def upload_file(self, resource_name: str, **kwargs) -> Object:
        """Upload a file to the bucket.

        Args:
            resource_name (str): The name of the file.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/s3/bucketobjectv2/#inputs)
        """
        opts = pulumi.ResourceOptions(parent=self)
        opts.merge(kwargs.pop("opts", None))

        return Object(resource_name=resource_name, opts=opts, **kwargs)

    @property
    def shortcut(self) -> str:
        arn = get_arn(self.arn)
        bucket_name = arn.resource.rsplit(":", 1)[-1]
        url = f"https://{arn.region}.console.aws.amazon.com/s3/buckets/{bucket_name}"
        return f"{url}?region={arn.region}&bucketType=general&tab=objects"

    @property
    def price(self) -> float:
        """Return the price per monthly for the resource in USD."""

        # todo: Amazon s3 pricing
        return 0.0
