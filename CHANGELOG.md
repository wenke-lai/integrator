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
