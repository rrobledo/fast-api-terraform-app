locals {
  app_name          = "challenge"
  container_definition = jsonencode({
    "name"        = "${local.app_name}-${var.environment}"
    "image"       = "${module.ecs.aws_ecr_repository.repository_url}:${var.IMAGE_TAG}"
    "essential"   = true
    "portMappings" = [{
      hostPort      = 80,
      protocol      = "tcp",
      containerPort = 80
    }]
  })
}