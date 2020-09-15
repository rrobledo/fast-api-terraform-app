module "ecs_instances" {
  source = "../ecs_instances"

  environment             = var.environment
  cluster                 = var.cluster
  instance_group          = var.instance_group
  private_subnet_ids      = var.private_subnet_ids
  aws_ami                 = var.ecs_aws_ami
  instance_type           = var.instance_type
  max_size                = var.max_size
  min_size                = var.min_size
  desired_capacity        = var.desired_capacity
  vpc_id                  = var.vpc_id
  iam_instance_profile_id = aws_iam_instance_profile.ecs.id
  key_name                = var.key_name
  load_balancers          = var.load_balancers
  depends_id              = var.depends_id
  custom_userdata         = var.custom_userdata
  cloudwatch_prefix       = var.cloudwatch_prefix
}

resource "aws_ecr_repository" "challenge_repo" {
  name                  = "challenge-${var.environment}"
  image_tag_mutability  = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}
resource "aws_ecr_repository_policy" "challenge-repo-policy" {
  repository = aws_ecr_repository.challenge_repo.name

  policy = <<EOF
            {
                "Version": "2008-10-17",
                "Statement": [
                    {
                        "Sid": "new policy",
                        "Effect": "Allow",
                        "Principal": "*",
                        "Action": [
                            "ecr:GetDownloadUrlForLayer",
                            "ecr:BatchGetImage",
                            "ecr:BatchCheckLayerAvailability",
                            "ecr:PutImage",
                            "ecr:InitiateLayerUpload",
                            "ecr:UploadLayerPart",
                            "ecr:CompleteLayerUpload",
                            "ecr:DescribeRepositories",
                            "ecr:GetRepositoryPolicy",
                            "ecr:ListImages",
                            "ecr:DeleteRepository",
                            "ecr:BatchDeleteImage",
                            "ecr:SetRepositoryPolicy",
                            "ecr:DeleteRepositoryPolicy"
                        ]
                    }
                ]
            }
            EOF
}

resource "aws_ecs_cluster" "cluster" {
  name = var.cluster
}
