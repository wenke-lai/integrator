from __future__ import annotations

from typing import TYPE_CHECKING

from pulumi_aws import s3

from diagrams.eraser import cloud_architecture as diagram

if TYPE_CHECKING:
    from .bucket import Bucket


class BucketPolicy(s3.BucketPolicy):
    def __init__(
        self, resource_name: str, bucket: Bucket, policy: str, **kwargs
    ) -> None:
        """Create a new S3 Bucket Policy.

        Args:
            resource_name (str): The name of the S3 Bucket Policy.
            bucket (Bucket): The S3 Bucket to attach the policy to.
            policy (str): The policy to attach to the S3 Bucket.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/s3/bucketpolicy/#inputs)
        """

        super().__init__(resource_name, bucket=bucket.id, policy=policy, **kwargs)

        self.diagram = diagram.Node(resource_name + "-bucket-policy", icon="aws-s3")
