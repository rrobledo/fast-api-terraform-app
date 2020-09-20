provider "aws" {
  region = var.region
}

module "network" {
  source               = "./modules/network"
  environment          = var.environment
  vpc_cidr             = var.vpc_cidr
  public_subnet_cidrs  = var.public_subnet_cidrs
  private_subnet_cidrs = var.private_subnet_cidrs
  availability_zones   = var.availability_zones
  depends_id           = ""
}

module "ecs" {
  source = "./modules/ecs"

  environment          = var.environment
  app_name             = local.app_name
  container_definition = local.container_definition
  cluster              = var.environment
  cloudwatch_prefix    = var.environment #See ecs_instances module when to set this and when not!
  vpc_id               = module.network.vpc_id
  vpc_cidr             = var.vpc_cidr
  public_subnet_ids    = module.network.public_subnet_ids
  public_subnet_cidrs  = var.public_subnet_cidrs
  private_subnet_ids   = module.network.private_subnet_ids
  private_subnet_cidrs = var.private_subnet_cidrs
  availability_zones   = var.availability_zones
  max_size             = var.max_size
  min_size             = var.min_size
  desired_capacity     = var.desired_capacity
  key_name             = aws_key_pair.ecs.key_name
  instance_type        = var.instance_type
  ecs_aws_ami          = var.ecs_aws_ami
  depends_id           = module.network.depends_id

  depends_on = [
    module.network
  ]
}

module "cognito" {
  source = "./modules/cognito"

  environment   = var.environment
  callback_urls = var.identity_callback_urls
  logout_urls   = var.identity_logout_urls
}

module "postgres" {
  source = "./modules/postgres"

  environment                         = var.environment
  vpc_id                              = module.network.vpc_id
  allocated_storage                   = 10
  storage_type                        = "gp2"
  storage_encrypted                   = false
  iam_database_authentication_enabled = true
  engine_version                      = "9.6.11"
  instance_class                      = "db.t2.micro"
  name                                = "challenge"
  username                            = "postgres"
  password                            = "postgres"
  subnet_ids                          = module.network.private_subnet_ids
}

resource "aws_key_pair" "ecs" {
  key_name   = "ecs-key-${var.environment}"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCtMljjj0Ccxux5Mssqraa/iHHxheW+m0Rh17fbd8t365y9EwBn00DN/0PjdU2CK6bjxwy8BNGXWoUXiSDDtGqRupH6e9J012yE5kxhpXnnkIcLGjkAiflDBVV4sXS4b3a2LSXL5Dyb93N2GdnJ03FJM4qDJ8lfDQxb38eYHytZkmxW14xLoyW5Hbyr3SXhdHC2/ecdp5nLNRwRWiW6g9OA6jTQ3LgeOZoM6dK4ltJUQOakKjiHsE+jvmO0hJYQN7+5gYOw0HHsM+zmATvSipAWzoWBWcmBxAbcdW0R0KvCwjylCyRVbRMRbSZ/c4idZbFLZXRb7ZJkqNJuy99+ld41 ecs@aws.fake"
}

variable "region" {}
variable "vpc_cidr" {}
variable "environment" {}
variable "max_size" {}
variable "min_size" {}
variable "desired_capacity" {}
variable "instance_type" {}
variable "ecs_aws_ami" {}

variable "private_subnet_cidrs" {
  type = list
}

variable "public_subnet_cidrs" {
  type = list
}

variable "availability_zones" {
  type = list
}

variable "identity_callback_urls" {
  type = list
}

variable "identity_logout_urls" {
  type = list
}

output "alb_target_group_arn" {
  value = module.ecs.alb_target_group_arn
}