Flask Events API – AWS Data Engineering Project
Overview
Designed with cost-efficient, serverless analytics and production-style data lake practices.

them as JSON logs in Amazon S3, and enables SQL analytics using Amazon Athena. Infrastructure is provisioned using Terraform.

Tech Stack

Python, Flask

AWS: EC2, S3, Athena, IAM

Terraform (Infrastructure as Code)

Architecture

Flask API (EC2) → JSON Logs → S3 (date-partitioned) → Athena (SQL analytics)

Key Features

Structured event logging (IP, user agent, path, method, timestamp)

Partitioned S3 data lake (year/month/day)

Athena table over JSON data

Least-privilege IAM access

Fully reproducible infrastructure with Terraform

Example Query
SELECT user_agent, COUNT(*) AS total_requests
FROM visit_logs
GROUP BY user_agent
ORDER BY total_requests DESC;

Outcome

Demonstrates practical experience with AWS-based data ingestion, storage, and analytics pipelines using production-oriented best practices.
