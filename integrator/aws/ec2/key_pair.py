from pathlib import Path

from pulumi_aws import ec2


class KeyPair(ec2.KeyPair):
    def __init__(self, resource_name: str, public_key: Path | str, **kwargs) -> None:
        """Create a new EC2 Key Pair.

        Args:
            name (str): The name of the EC2 Key Pair.
            **kwargs: [additional arguments](https://www.pulumi.com/registry/packages/aws/api-docs/ec2/keypair/#inputs)
        """
        with open(public_key, "r", encoding="utf-8") as fr:
            super().__init__(resource_name, public_key=fr.read(), **kwargs)
