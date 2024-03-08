from pulumi_aws import s3

from diagrams.eraser import cloud_architecture as diagram


class Object(s3.BucketObjectv2):
    def __init__(self, resource_name: str, **kwargs) -> None:
        """Create a new S3 Object.

        Args:
            resource_name (str): The name of the S3 Object.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/s3/bucketobjectv2/#inputs)
        """

        super().__init__(resource_name, **kwargs)

        self.diagram = diagram.Node(resource_name, icon="aws-simple-storage-service")
