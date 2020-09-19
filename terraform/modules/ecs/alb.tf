module "alb" {
  source = "./alb"

  environment       = var.environment
  cluster           = var.cluster
  instance_group    = var.instance_group
  alb_name          = "${var.environment}-${var.cluster}"
  vpc_id            = var.vpc_id
  health_check_path = "/health"
  public_subnet_ids = var.public_subnet_ids
  autoscaling_group_id = module.ecs_instances.aws_autoscaling_group_id
}

resource "aws_security_group_rule" "alb_to_ecs" {
  type                     = "ingress"
  from_port                = 0
  to_port                  = 61000
  protocol                 = "TCP"
  source_security_group_id = module.alb.alb_security_group_id
  security_group_id        = module.ecs_instances.ecs_instance_security_group_id
}
