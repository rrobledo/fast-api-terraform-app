region = "us-east-1"

vpc_cidr = "10.0.0.0/16"

environment = "dev"

public_subnet_cidrs = ["10.0.0.0/24", "10.0.1.0/24"]

private_subnet_cidrs = ["10.0.50.0/24", "10.0.51.0/24"]

availability_zones = ["us-east-1a", "us-east-1b"]

max_size = 2

min_size = 2

desired_capacity = 2

instance_type = "t2.micro"

ecs_aws_ami = "ami-275ffe31"

identity_callback_urls = ["http://localhost/callback"]

identity_logout_urls = ["http://localhost/signout"]