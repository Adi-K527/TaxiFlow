resource "aws_ecr_repository" "model_repo" {
  name = var.repo_name
}