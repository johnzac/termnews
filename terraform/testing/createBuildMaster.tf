resource "aws_instance" "buildMaster"
{
ami = "ami-efd0428f"
instance_type = "t2.micro"
vpc_security_group_ids = ["${aws_security_group.public-sg.id}"]
key_name = "key-name"
subnet_id="${aws_subnet.public_subnet-us-west-2b.id}"
private_ip="192.168.104.5"
user_data = "${file("userData")}"
tags {
    Name = "termnews-test"
  }

}
