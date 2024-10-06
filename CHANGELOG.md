## 0.5.0 (2024-10-06)

### Feat

- remove diagrams package

## 0.4.0 (2024-09-23)

### Feat

- **aws.elasticache**: create serverless redis resources
- **aws.apigateway**: create rest-api resources
- **aws.acm**: add `.shortcut` and `.price` to certificate resource
- **aws.route53**: add `.price` to zone resource
- **aws.route53**: add `.shortcut` to return the url of a zone
- **aws**: add set_availability_zones() to limit AZs to be used in VPC
- **aws**: add security-group arg to launch-template for creating ASG
- **aws**: add secret resource to secrets manager
- **aws**: add aurora-mysql serverless v2 and subnet-group resources to rds

### Fix

- **aws.cloudfront**: add `price_class` props to distribution resource
- **aws.cloudfront**: set HTTP version to HTTP/2 by default for distribution
- **aws.cognito**: add a method to user-pool to create user-pool-client
- **aws.alb**: set `enable_deletion_protection` to true by default
- **aws.opensearch**: add `engine_version` to ES Domain
- **aws.rds**: add `engine_version` args to Aurora Cluster
- **aws.ec2**: change the `key_pair` of launch-template to a optional parameter
- **aws.cloudfront, aws.s3**: add `.shortcut` and `.price` attributes
- use __getattr__ instead of __getattribute__
- **aws.acm,aws.route53**: add __getattribute__ to export attrs from specify resources
- **aws.acm**: fix the missed import for ExistingCertificate
- **aws.acm**: add ExistingCertificate to look up existing certifcate resource
- **aws.route53**: remove `._resource` from Zone
- **aws.route53**: enhance zones and records
- **aws.rds**: use serverless-v2-instance instead of cluster instance
- **aws.rds**: add the cluster-instance resource for serverless v2 cluster
- **aws**: use ipv4 instead of dual by default for rds cluster
- **aws**: fix a typo for Listener of alb
- **aws**: add shortcut args to Group of autoscaling
- **aws**: add import for aurora-mysql serverless v2 to rds

### Refactor

- **aws.acm, aws.route53**: update coding style

## 0.3.0 (2024-03-09)

### Feat

- **aws.opensearch**: improve the domain for easier usage
- **aws.cloudwatch**: add log-group and log-group-resource resources

### Fix

- **aws**: use resource-name instead of name
- **aws.ecr**: fix the conflict between name and resource-name
- **aws**: add imports for main resources
- **aws.cloudfront**: update the import path fo resources
- **aws.cloudfront**: add default cache-policy, ordered-cache-policy and response-header-policy
- **aws.cloudfront**: enhance distribution resources
- **aws.acm**: fix the wrong import

### Refactor

- **aws.opensearch**: remove es-log-group-resource

## 0.2.0 (2024-09-23)

### Feat

- **aws.elasticache**: create serverless redis resources
- **aws.apigateway**: create rest-api resources
- **aws.acm**: add `.shortcut` and `.price` to certificate resource
- **aws.route53**: add `.price` to zone resource
- **aws.route53**: add `.shortcut` to return the url of a zone
- **aws**: add set_availability_zones() to limit AZs to be used in VPC
- **aws**: add security-group arg to launch-template for creating ASG
- **aws**: add secret resource to secrets manager
- **aws**: add aurora-mysql serverless v2 and subnet-group resources to rds

### Fix

- **aws.cloudfront**: add `price_class` props to distribution resource
- **aws.cloudfront**: set HTTP version to HTTP/2 by default for distribution
- **aws.cognito**: add a method to user-pool to create user-pool-client
- **aws.alb**: set `enable_deletion_protection` to true by default
- **aws.opensearch**: add `engine_version` to ES Domain
- **aws.rds**: add `engine_version` args to Aurora Cluster
- **aws.ec2**: change the `key_pair` of launch-template to a optional parameter
- **aws.cloudfront, aws.s3**: add `.shortcut` and `.price` attributes
- use __getattr__ instead of __getattribute__
- **aws.acm,aws.route53**: add __getattribute__ to export attrs from specify resources
- **aws.acm**: fix the missed import for ExistingCertificate
- **aws.acm**: add ExistingCertificate to look up existing certifcate resource
- **aws.route53**: remove `._resource` from Zone
- **aws.route53**: enhance zones and records
- **aws.rds**: use serverless-v2-instance instead of cluster instance
- **aws.rds**: add the cluster-instance resource for serverless v2 cluster
- **aws**: use ipv4 instead of dual by default for rds cluster
- **aws**: fix a typo for Listener of alb
- **aws**: add shortcut args to Group of autoscaling
- **aws**: add import for aurora-mysql serverless v2 to rds

### Refactor

- **aws.acm, aws.route53**: update coding style

## 0.3.0 (2024-03-09)

### Feat

- **aws.opensearch**: improve the domain for easier usage
- **aws.cloudwatch**: add log-group and log-group-resource resources

### Fix

- **aws**: use resource-name instead of name
- **aws.ecr**: fix the conflict between name and resource-name
- **aws**: add imports for main resources
- **aws.cloudfront**: update the import path fo resources
- **aws.cloudfront**: add default cache-policy, ordered-cache-policy and response-header-policy
- **aws.cloudfront**: enhance distribution resources
- **aws.acm**: fix the wrong import

### Refactor

- **aws.opensearch**: remove es-log-group-resource

## 0.2.0 (2024-02-29)

### Feat

- add get-my-ip to global
- **aws.ec2, aws.iam**: implement launch-template, role and policy resources
- **aws.ec2**: implmented shortcuts to create igw, subnet and security-group resources via Vpc
- add azure, gcp, github, gitlab and grafana into integrator
- **aws.sns, aws.sqs**: add topic and queue resources
- **aws.ses**: add template resource
- **aws.scheduler**: add schedule and schedule-group resources
- **aws.s3**: add bucket and object resources
- **aws.route53**: add zone and record resources
- **aws.lambda**: add function resource
- **aws.kms**: add key resource
- **aws.iam**: add user, group, role and policy resources
- **aws.ecs**: add cluster and task-definition resources
- **aws.ecr**: add repository interface
- **aws.cognito**: add user pool interfaces
- **aws.dynamodb**: add table interface
- **aws.cloudfront**: add distribution and policies interfaces
- **aws.asg**: add group and policy interfaces
- **aws.dlm, aws.ec2**: add interfaces
- **aws.alb**: add load-balancer, listener, target-group resources
- **aws.acm**: add certificate resource
- initial project

### Fix

- **aws.ec2**: give the default-route-rule of security-group a unique name
- **aws.ec2**: resolve the conflicting opts parameters between the instance and launch-template
- **aws.iam**: set the parent of a role profile to the role itself by default
- **aws.ec2**: add tag name to vpc, subnet, security-group and instance
- **aws.ec2**: fix the wrong types of security-group rule
- **aws.ec2**: add image prop to launch-template
- **aws.ec2**: use id, key-pair object has no attribute name
- **aws.ec2**: add import shortcut for user-data
- **aws.iam**: attach policy automatically when create the policy via role
- **aws.ec2**: add the import of key-pair to aws.ec2
- **aws.ec2**: add public-key prop to KeyPair
- **aws.ec2**: add availability-zones to Vpc
- **aws.ec2**: remove the suffix of naming from internet-gateway and default-route
- **aws.ec2**: add .destination_cidr_block to gateway route
- **aws.alb**: fix typos and import errors

## 0.1.0 (2024-02-25)
