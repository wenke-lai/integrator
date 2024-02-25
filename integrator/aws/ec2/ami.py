from pulumi_aws import ec2


class Ubuntu:

    @property
    def jammy_22(self) -> ec2.AwaitableGetAmiResult:
        return ec2.get_ami(
            most_recent=True,
            owners=["099720109477"],
            name_regex="ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*",
        )
