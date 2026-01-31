data "aws_iam_role" "existing_ec2_role" {
  name = "ec2-dynamodb-role"
}

resource "aws_iam_policy" "terraform_policy" {
  name = "terraform-s3-athena-policy"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [

      # --- S3 access for logs & athena results ---
      {
        Effect = "Allow",
        Action = [
          "s3:PutObject",
          "s3:GetObject",
          "s3:ListBucket",
          "s3:GetBucketLocation"
        ],
        Resource = [
          "arn:aws:s3:::flask-visit-logs-2026",
          "arn:aws:s3:::flask-visit-logs-2026/*"
        ]
      },

      # --- Athena & Glue ---
      {
        Effect = "Allow",
        Action = [
          "athena:*",
          "glue:*"
        ],
        Resource = "*"
      },

      # --- Allow Terraform to manage this policy itself ---
      {
        Effect = "Allow",
        Action = [
          "iam:GetPolicy",
          "iam:GetPolicyVersion",
          "iam:CreatePolicyVersion",
          "iam:DeletePolicyVersion"
        ],
        Resource = "arn:aws:iam::969744962288:policy/terraform-s3-athena-policy"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "attach_policy" {
  role       = data.aws_iam_role.existing_ec2_role.name
  policy_arn = aws_iam_policy.terraform_policy.arn
}

