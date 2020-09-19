output "alb_target_group_arn" {
  value = module.alb.alb_target_group_arn
}

output "aws_ecr_repository" {
  value = aws_ecr_repository.challenge_repo
}
