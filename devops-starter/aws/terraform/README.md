# AWS Terraform Baseline

This Terraform setup creates:

- ECR repository for container images
- CloudWatch log group for application logs

## Usage

```bash
cd devops-starter/aws/terraform
terraform init
terraform plan -var='environment=staging'
terraform apply -var='environment=staging'
```

## Extend Next

- Add VPC, subnets, NAT/IGW
- Add EKS cluster and node groups
- Add IAM roles for service accounts
- Add ALB ingress controller resources
