from pulumi_aws import ec2


class KeyPair(ec2.KeyPair):
    def __init__(self, name: str, **kwargs) -> None:
        """Create a new EC2 Key Pair.

        Args:
            name (str): The name of the EC2 Key Pair.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ec2/keypair/#inputs)
        """
        super().__init__(name, **kwargs)
