output "ecr_repository_url" {
  value       = aws_ecr_repository.app.repository_url
  description = "ECR repository URL"
}

output "cloudwatch_log_group_name" {
  value       = aws_cloudwatch_log_group.app.name
  description = "CloudWatch log group name"
}
