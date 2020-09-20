output "alb_target_group_arn" {
  value = module.alb.alb_target_group_arn
}

output "aws_ecr_repository" {
  value = aws_ecr_repository.challenge_repo
}

output "aws_cloudwatch_log_group_docker" {
  value = module.ecs_instances.aws_cloudwatch_log_group_docker
}

output "alb_dns_name" {
  value = module.alb.alb_dns_name
}
