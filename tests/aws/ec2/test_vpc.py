import pulumi
import pulumi_aws as aws

from integrator.aws import ec2

# pylint: disable=redefined-outer-name


class PulumiMocks(pulumi.runtime.Mocks):
    def new_resource(self, args: pulumi.runtime.MockResourceArgs):
        return [args.name + "_id", args.inputs]

    def call(self, args: pulumi.runtime.MockCallArgs):
        return {}


def setup_function():
    pulumi_mocks = PulumiMocks()
    pulumi.runtime.set_mocks(pulumi_mocks, preview=False)
    yield pulumi_mocks


@pulumi.runtime.test
def test_create_vpc():
    vpc = ec2.Vpc("test")
    assert isinstance(vpc, aws.ec2.Vpc)

    def check_vpc(args):
        cidr_block, enable_dns_hostnames = args
        assert cidr_block == "10.0.0.0/16"
        assert enable_dns_hostnames, "vpc should enable dns hostnames"

    pulumi.Output.all(vpc.cidr_block, vpc.enable_dns_hostnames).apply(check_vpc)


@pulumi.runtime.test
def test_vpc_creates_internet_gateway():
    vpc = ec2.Vpc("test")
    igw, default_route = vpc.create_internet_gateway("test")
    assert isinstance(igw, aws.ec2.InternetGateway)
    assert isinstance(default_route, aws.ec2.Route)


@pulumi.runtime.test
def test_vpc_creates_public_subnet():
    vpc = ec2.Vpc("test")
    public = vpc.create_public_subnet("public", "us-west-2a", "10.0.0.0/24")
    assert isinstance(public, aws.ec2.Subnet)

    def check_public_subnet(args):
        availability_zone, cidr_block, map_public_ip_on_launch = args
        assert availability_zone == "us-west-2a"
        assert cidr_block == "10.0.0.0/24"
        assert map_public_ip_on_launch, "public subnet should map public ip on launch"

    pulumi.Output.all(
        public.availability_zone,
        public.cidr_block,
        public.map_public_ip_on_launch,
    ).apply(check_public_subnet)


@pulumi.runtime.test
def test_vpc_creates_private_subnet():
    vpc = ec2.Vpc("test")
    private = vpc.create_private_subnet("private", "us-west-2b", "10.0.1.0/24")
    assert isinstance(private, aws.ec2.Subnet)

    def check_private_subnet(args):
        availability_zone, cidr_block, map_public_ip_on_launch = args
        assert availability_zone == "us-west-2b"
        assert cidr_block == "10.0.1.0/24"
        assert (
            not map_public_ip_on_launch
        ), "private subnet should not map public ip on launch"

    pulumi.Output.all(
        private.availability_zone,
        private.cidr_block,
        private.map_public_ip_on_launch,
    ).apply(check_private_subnet)


def test_vpc_creates_security_group():
    vpc = ec2.Vpc("test")
    sg = vpc.create_security_group("test")
    assert isinstance(sg, aws.ec2.SecurityGroup)
