#creating our vpc
resource "aws_vpc" "demoAppVpc" {
    cidr_block = "192.168.0.0/16"
   enable_dns_support = "true"
   enable_dns_hostnames = "true"
}

#creating our subnets
#creating main public subnet
resource "aws_subnet" "public_subnet-us-west-2a"
{
vpc_id="${aws_vpc.demoAppVpc.id}"
cidr_block="192.168.101.0/24"
map_public_ip_on_launch ="true"
availability_zone = "us-west-2a"
tags
{
name = "public-subnet"
}
}

resource "aws_subnet" "public_subnet-us-west-2b"
{
vpc_id="${aws_vpc.demoAppVpc.id}"
cidr_block="192.168.104.0/24"
map_public_ip_on_launch ="true"
availability_zone = "us-west-2b"
tags
{
name = "public-subnet"
}
}



resource "aws_internet_gateway" "igw"
{
vpc_id="${aws_vpc.demoAppVpc.id}"
tags
{
name="igw demoApp"
}
}
resource "aws_route_table" "public-subnet-route-table"
{
vpc_id="${aws_vpc.demoAppVpc.id}"
route
{
cidr_block="0.0.0.0/0"
gateway_id="${aws_internet_gateway.igw.id}"
}
tags
{
name = "public-route-table"
}
}
resource "aws_route_table_association" "public-subnet-route-us-west-2a"
{
subnet_id = "${aws_subnet.public_subnet-us-west-2a.id}"
route_table_id="${aws_route_table.public-subnet-route-table.id}"
}

resource "aws_route_table_association" "public-subnet-route-us-west-2b"
{
subnet_id = "${aws_subnet.public_subnet-us-west-2b.id}"
route_table_id="${aws_route_table.public-subnet-route-table.id}"
}


