resource "aws_ecs_task_definition" "challenge-task" {
  family                   = var.app_name
  requires_compatibilities = ["EC2"]
  cpu                      = 256
  memory                   = 512
  container_definitions    = "[${var.container_definition}]"
}

resource "aws_ecs_service" "challenge-service" {
  name            = "${var.app_name}-${var.environment}"
  cluster         = aws_ecs_cluster.cluster.id
  launch_type     = "EC2"
  task_definition = aws_ecs_task_definition.challenge-task.arn
  desired_count   = var.desired_capacity

  load_balancer {
    target_group_arn = module.alb.alb_target_group_arn
    container_name   = "${var.app_name}-${var.environment}"
    container_port   = 80
  }

  depends_on = [module.alb]
}
