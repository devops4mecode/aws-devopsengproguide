# AWS DevOps Engineer Professional (DOP-C01)

### Introduction

<br>
<p align="center"><img src="./assets/AWS DevOps Engineer Professional (DOP-C01) - Study Guide.png"></p>
<br>

<details><summary> <b>Part 1: SDLC Automation</b></summary>
<br>

### What To Learn?
- Automate a CI/CD pipeline by implementing the necessary concepts.
Determine the best methods for implementing source control
Integrate and automate testing concepts.
- Build and manage artefacts in a secure manner by utilising these concepts.
- Learn how to use AWS Services to implement deployment and delivery strategies (e.g., A/B testing, Blue/Green testing, Canary testing, Red/Black testing)

### AWS CodePipeline

- AWS CodeCommit

	- Repository Tags

		- Help to identify and organize your AWS resources

	- Identity Policies based on tags

		- Allow and denies action on CodeCommit Repo based on tags associated with CodeCommit repo.
		- Example

	- Integrations

		- AWS Lambda
		- EventBridge
		- CloudTrails
		- CodeBuild
		- AWS KMS
		- etc.

	- Monitoring & Logging

		- Allow Admin captures insight into activities by users
		- Creating a dashboard

	- Notification Rules

		- Get notify whenever there changes on specific action on repo

			- Comments
			- Apporval
			- Pull Request (PR)
			- Branches & tags

	- CodeCommit Policies

		- Managed Policies

			- AWSCodeCommitFullAccess
			- AWSCodeCommitPowerUser
			- AWSCodeCommitReadOnly

		- Data Protection

	- Approval Rule Template

- AWS CodeBuild

	- Concepts

		- Build Project
		- Source
		- Environment
		- S3 and SNS

	- Security 

		- AWS IAM Access
		- Artifact Encryption 
		- AWS CodeBuild Role

- AWS CodeDeploy

	- AppSpec Hooks

		- ApplicationStop
		- DownloadBundle
		- BeforeInstall
		- Install
		- AfterInstall
		- ApplicationStart
		- ValidateService

	- Deployment Policies

		- AllAtOnce

			- disadv: When update is failed, app not accessible

		- Rolling

			- disadv: When update is failed, not at full capacity.

		- Rolling with additional Batch

			- adv: Full capacity even update is failed

		- Immutable

			- Deploy newer ver. of app in completely new server under auto-scaling group(ASG)

		- Traffic Splitting
		- Blue/Green

			- BLUE

				- Prod receiving LIVE traffic

			- GREEN

				- Parallel env running diff ver of the apps

	- Deployment/Delivery Strategies

		- All-At-Once
		- Rolling Deploy
		- Blue-Green
		- Canary Release

### Elastic Beanstalk(EB)

- EB CLI
- EB extension

	- .ebextensions
	- YAML file
	- Allow us to customize all the things that is needed for apps

- Commands

	- Container

		- Ensure that your command is run on only one instance
		- leaders_only: true
		- Purpose: Creation of DB. running DB migration script & etc.
		- Run AFTER the apps & web server is set up & the apps version file is extracted

	- Command

		- Run BEFORE the apps & web server is set up & the apps version file is extracted

- Canary Deployment

	- Is a process where we deploy a few features and shift % of traffic to new feature to perform some analysis to see is the feature successful.

### Lambda

- Versioning
- Alias
- Spliting Traffic
- Lambda@Edge

	- Viewer Request
	- Origin Request
	- Viewer Response
	- Origin Response
	- CloudFront Cache

### AWS ECR

- fully managed Docker registry that makes it easy for developer to store, manage, & deploy docker images.
- Create ECR repository
- Login to ECR
- Push/Pull ECR docker images

### 

- It is a container orchestration service that support Docker containers and allow you to easily run and scale containerized apps on AWS
- EC2
- Fargate

### AWS Fargate

- Run containerized apps without provisioning, monitor or manage the underlying  AWS resource

### Jenkins

- Is an open-source automation server which allows us to automate wide variety of things which includes the entire CI/CD pipeline.
- Distributed Builds(worker nodes)
- Jenkins Plugins

### Git Service

- Concepts

	- Repository

		- The place where all code changes are store and versioning.

	- Branches

		- Master Branch
		- Feature branch

	- Commit

		- Push new code updates to the repository

	- Pull Request (PR)

		- Merge Request (MR)
		- PR Validations

- Git Strategy

	- Trunk Based Development(TBD)

		- All works is done on Master branch
		- Pros

			- Very small changes
			- Continuous code merge
			- Increase delivery throuhput

		- Cons

			- Many Tests

	- GitHub Flow

		- All work is done on individual branch
		- Pros

			- Master always releasable
			- Short live branches

		- Cons

			- Master not always up to date
			- Large changes to Master

	- GitFlow

		- Branches

			- Feature merge to develop
			- Release branches
			- Feature and Hotfix branches

		- Pros

			- Master is always releasable
			- Strict Control

		- Cons

			- Master not always up to date
			- Large changes to Master
			- Complicated to enforce

	- Environment Branching

		- Branch per environment
		- Change all to one branch
		- Gradual release to Prod
		- Pros

			- Each of env have it own branch
			- Prod always is releasable

		- Cons

			- Prod not always up to date
			- Large change to Prod
			- Multiple merge per release

### Automated Tests

- Linting
- Unit-Test

	- Conducted by Developers and test the unit of code(module, component) that they developed.

- Integration Test

	- Test is the approach in which multiple components of apps are combined and tested in a group

- Regression Test

	- To test the new functionality 
	- Re-run that apps previously passed, to ensure that new features not re-introduce old defects or create new ones

- Test Driven Development (TDD)

	- Practice of writing tests that matches intended behaviour, before you write the codes.

- Continuous Testing

	- Artifact Test

		- Unit-Test
		- Vul Image Scanning
		- SAST

	- Environment Validation

		- Load Testing
		- Penetration Test
		- IAST/DAST

### Whitepaper: Containerized Microservices

- Decoupled
- Single Function
- Well-Defined API's
- 12-Factor App

	- Isolation Dependencies 
	- Ephemeral(Disposable)
	- Scalability (Concurrency)

- Org Structure 

	- Autonomous Teams
	- Own Microservices all the way to Prod

- Product not Project

	- Automation
	- Self-Service
	- Continuous Integration
	- Continuous Delivery

- Smart Endpoints Dump Pipes

	- Communication  between services

		- Request/Response
		- Publish/Subcribe

- Decentraliszed Governance

	- Freedom to choose dependency 
	- Freedom to choose build tools

- Decentralized Data Management

	- Freedom to choose data tools
	- No Shared data sources

- Design for Failure

	- Disposable (stateless)
	- Latency and timeouts to be expected
	- Able to failover to other region/dc
	- Self-Healing
	- Logs as event-streams
</details>
<br>
<details><summary> <b>Part 2: Config. Management & IaC</b></summary>
<br>

### What To Learn?
- Identify the most appropriate deployment services based on the actual requirements of the project
- Determine application and infrastructure deployment models based on the needs of your company.
- Automate resource provisioning using security concepts.
- On a deployment, determine how to use lifecycle hooks.
- Use AWS configuration management tools and services to learn about system management concepts.

### Elastic Container Service (ECS)

- Task Def
- Service
- AWS CodePipeline Integration(CD-Deploy)
- Security 

	- Host layer

		- Security Group
		- NACL's
		- EC2 Service Role
		- Network Isolation
		- Subtopic 5

			- Inspector
			- 3rd party Sec Tools

	- Container Layer

		- Task Role
		- Port Mappings
		- 3rd party Sec Tools

	- Service Layer

		- AWS IAM
		- CloudTrail

### 12 Factor Apps Pattern

- Codebase
- Dependencies
- Config
- Backing services
- Build, release, run
- Processes
- Port binding
- Concurrency
- Disposability
- Dev/prod parity
- Logs
- Admin processes

### AWS Lambda

- Concepts

	- Serverless
	- Triggers
	- Runtime
	- Deployment Package
	- Concurrency 

- Features

	- Version and Alias
	- Concurrency limits
	- Layers-custom runtimes
	- Step Functions
	- Extension

- Quotas

	- Memory  - 1024MB
	- Timeout -  900 seconds(!5mins)
	- Deployment Package
500MB Zipped and 250mB Unzipped
	- /tmp strg: 512MB

- Security

	- IAM

		- Execution Role
		- User Access

	- Data

		- Encryption in Trainsit
		- Encryption at Rest
		- Env. Variable SSM/Secret Mgr

### DynamoDB

- Key-value memory database

### Elasticache

- memory cache management

### AWS API Gateway

- Deploy and Manage an API
- Multiple stages
- Request throttling
- RESTful, HTTP, and WebSocket API
- Amazon manages the underlying resources 
- Use-Cases

	- Serverless API

		- AWS Lambda

	- Direct Public request to private resources 

		- AWS ECS, LBs,etc
</details>
<br>
<details><summary> <b>Part 3: Monitoring & Logging</b></summary>
<br>

### What To Learn?

- Based on the project's actual needs, select the best deployment services.
- Assess your company's requirements to determine the best model for deploying applications and infrastructure.
- Security concepts can be used to automate the provisioning of resources.
- Determine how to use lifecycle hooks during a deployment.
- Learn about system management with the help of AWS tools and services.

### CloudWatch

- CloudWatch Logs

	- Integrated with AWS services such Lambda, CodeBuild, etc
	- Use CloudWatch Agent for EC2
	- Log Groups
	- Log Streams

- CloudWatch Events (EventBridge)

	- What it is?

		- Integrated with AWS services such AWS CodePipeline & AWS CloudTrail
		- Also known as EventBridge
		- Support Custom Events
		- Help automate actions in AWS

- CloudWatch Metrics

	- Integrated with AWS services such Lambda, EC2,etc
	- Use Agent for custom metrics
	- CloudWatch Dashboard

- CloudWatch Alarms

	- utilise metrics and events
	- Can use limits, statistical analysis ,anomaly detection 

### AWS Kenesis

- Video Stream
- Data Stream

	- Stream of data can be ingested at low latency
	- Short term retention of data
	- Manual scaling ans setup
	- Benefit

		- Customisable consumers

- Data Firehose

	- Real-time streaming of data into AWS S3, AWS RedShift, ElasticSearch or Splunk
	- No retention of data
	- Automate Scaling and setup

- Data Analytics 

### AWS RedShift

- Data Warehouse
- Centralize Logs

	- Apps Logs
	- Network Logs
	- Infra logs

- Columnar data store

### AWS QuickSight

- Business Intelligence data tool
- Visualisation, analysis, & reporting on metrics by querying  AWS RedShift
- Correlating multiples logs

### AWS Elasticsearch

- Managed ELK Stack
- Centralise logs, reporting, alerting, metrics, and analytics 
- Automated backup, upgrades, scaling, and maintenance
- Terms

	- Cluster(Domain)
	- Indice/Index
	- Types
	- Document with properties

### AWS CloudTrail

- API events in AWS can be recorded and logged. Uses AWS S3 as destination
- Security

	- AWS S3 key by default encryption key
	- KMS

- Features

	- Data Events
	- CW Log integration 
	- Account centralization
	- CloudTrail Insights 

### AWS Config

- What is it?

	- Track config of AWS resources over time
	- Gives insight into policy compliance 
	- Reactive response, not Proactive

- Terms

	- Resources

		- Each item in AWS

	- Config Item

		- Config at specific time 

			- Basic config., specific config. , releationship, AWS CloudTrail ID's , Metadata

	- Config Rules
	- Conformance Packs

		- Package of Rules + Remediation actions

	- Evaluation 

		- Determines one rule against one resource ( changes determined by evolutions)

	- Aggregator 

		- Used to centralize dashboard

- Features

	- multiple account and region
	- Integration with ServiceNow and Jira Service Desk

### Trusted Advisor

- What it is?

	- Included in Support Plan (Developer)
	- Scan and Alert for best practices
	- Weekly scan and email, but manually  scan more frequently 

- Features

	- Security Checks 

		- Security Groups
		- Public Snapshots
		- AWS S3 Buckets

	- Cost Optimisation 
	- Fault-Tolerance 
	- Performance 
	- Service Limits

### AWS X-Ray

- Purpose

	- Distributed tracing system
	- Helps analyze and troubleshoot bugs
	- Understand performance
	- End-to-end view of requests
	- Component map of apps

- Components

	- AWS X-Ray SDK/API: Implemented in the code
	- AWS X-Ray Daemon: Implemeneted at the server layer proxying request from code to AWS X-Ray

- Service to monitor?

	- API Gateway
	- App Mesh
	- AppSync
	- EventBridge
	- SNS
	- SQS
	- S3
	- EC2
	- ECS
	- Beanstalk
	- Lambda

- Integration 

	- AWS Config
	- CloudTrail
	- CloudWatch
	- EventBridge
	- Load Balancing

### Tagging Resources 

- Organization
- Cost Allocation
- Automation
- Ops Support
- Control Access
- Security Risk Management

### Resource Group & tag Editor

- Implement/Update Tag over the regions
- Create Resource Group and Tag Group
</details>
<br>
<details><summary> <b>Part 4: Policies & Standard Automation</b></summary>
<br>

### What To Learn?
- Logging, metrics, monitoring, testing, and security standards can be enforced by applying the necessary concepts.
- Determine how to cut costs by automating processes.
- Utilize the concepts necessary to put governance strategies into action

### AWS System Manager

- OpsCenter

	- Centralizzed dashboard to troubleshoot issue
	- Aggresgates data from AWS Config, AWS CloudTrail, AWS CloudWatch

- Inventory

	- Collects Information about AWS EC2 instances and software installed on them
	- Collect information on network, config., files, server roles, etc.

- Parameter Store & Documents

	- Storing config. data
	- Plain text or encrypted 
	- scripts
	- Can have logic so single script can handle multiple scenarios(Windows/Linux)

- Automation & Run Command

	- Automate the roll out of playbooks 
	- Roll back automatically if erros
	- Automates common tasks
	- No Need to login to the server at all

- Session Manager

	- Login to system to run CLI commands
	- Removes the need to SSH Keys
	- No Need for the ports to be oponed
	- Access is controlled by IAM

- Patch Manager

	- Automates patching on server software

- State Manager

	- Remotely manage config of server (Firewall config., server settings, etc)

- Distributor 

	- Centralized place to retrieve packages and apps that you may want to automatically install/update

### AWS Secret Manager

- Encrypted  Credential manager
- App's retrieval of password
- Automated password rotation

### AWS Inspector

- Network Reachability
- Host-based security scan

	- CVE's
	- CIS Benchmark
	- Security best-practice 

### AWS Service Catalog

- Templatized resources that end-users can deploy
- Enforces standards
- User restrictions
- Distribution 
- Use-cases

	- Product: Collection of resources
	- Portfolio : Collection of Products
	- UC1: tool that you want to allow users to deploy
	- UC2: allowing users to deploy their apps
</details>
<br>
<details><summary> <b>Part 5: Incident & Event Response</b></summary>
<br>
### What To Learn?
- Determine the source of the problem and the best course of action for resolving it
- Decide on a way to automate alerting and event management
- Implement the concepts necessary for automated healing to take place.
- Integrate key event-driven automation concepts into your work

### Troubleshooting 

- Process

	- Find the issue
	- Find the thing that are working
	- Look for the things you can change
	- Implementation details

- Tools

	- Monitoring

		- CloudWatch agent/logs

	- Alerting

		- Events
		- Alerts

	- Remediation

		- AWS Lambda
		- AWS System Manager

	- Prevention

		- AWS IAM
		- AWS CloudFormation

### Elastic Load Balancing

- Application Load Balancer (ALB)

	- Layer 7 LB
	- Port 80/443
	- HTTP, HTTPS, gRPC
	- SSL/HTTPS termination
	- Integration with AWS Cognito and OpenID Connect
	- Can route to AWS Lambda

- Network Load Balancer (NLB)

	- Layer 4 LB
	- Port: ALL
	- SSL/HTTPS termination

- Gateway Load Balancer

	- Layer 3 Gateway + Layer 4 LB
	- Made for in-line network analysis appliances

- Classic Load Balancer

	- Layer 4/7 L:B
	- Protocols: TCP, SSL/TLS, HTTP, HTTPS
	- SSL/HTTPS termination
	- Primary for AWS EC2 classic Instance

### EC2 Auto-Scaling

- Only support AWS EC2
- Can perform Step and Scheduled scaling
- Creates and configure Auto-Scaling-Group
- Support multiple-Purchase model
- Support Multiple AZs
- Support Multi-instance sizes in a single apps
- Security

	- AWS IAM

		- Service Roles
		- User Roles

	- KMS encryption for Volumes

- Cost Optimization

	- On-Demand, Reserved, Spot Instances - Combined
	- Multiple instance types

### AWS Auto-Scaling

- Support AWS EC2, ECS, DynamoDB, Aurora
- Only scales based on target tracking scaling policies
- Creates and manages CloudWatch alarms and triggering scaling
- Predictive scaling for EC2
- Automatically scan for scalable services
</details>
<br>
<details><summary> <b>Part 6: High Availability (HA), Fault-Tolerance, & Disaster Recovery (DR)</b></summary>
<br>

### What To Learn?
- Determine whether multi-AZ or multi-region architectures are appropriate for your application.
- Learn how to implement high availability, scaling, and fault tolerance
- Use business requirements (e.g., RTO/RPO, cost) to select the best services.
- Learn how to create and implement disaster recovery plans that are automated.
- Determine what areas of a deployment may be at risk.

### Multi-AZ

### AWS Region

### High-Availability (HA)

- Global Services

	- AWS S3
	- AWS IAM
	- AWS Route53
	- AWS CloudFront

- Regional Services

	- S3 Data
	- AutoScaling
	- DynamocDB
	- Load Balancing
	- VPC

### Scalability 

- Load Balancer
- EC2 Auto-Scaling
- AWS Auto-Scaling
- CloudWatch
- CloudFront
- Elasticache

### Fault-Tolerance

- Route53
- S3
- CloudWatch
- EC2 Auto-Scaling
- AWS Auto-Scaling

### Disaster Recovery (DR)

- RTO & RPO

	- RTO:Recovery Time Objective

		- The max acceptable delay between the interruption of service and restoration of service

	- RPO: Recovery Point Objective

		- is the maximum acceptable amount of time since the last data recovery point.

- RDS

	- Automated backups
	- DB Snapshits
	- Multi-AZ
	- Read Replica

- EC2 & EBS
- DynamoDB

	- Snapshits and Point-in0-time recovery
	- Global Table(Cross-region replication)

- Route53

	- Health Check for endpoints 
	- Active-Active and Passive routing
	- Round-robin
	- Weighted Routing

- S3

	- Durability/Availability 
	- Cross-Region Replication (CRR)
	- Archieve Access Tier are moved to the Frequent  Access tier in 3-5 hours
	- Deep Archive tiear are moved to Frequent Access tier within 12 hours
	- Glacier Retrieval

- Strategies

	- AWS Lambda: Snapshot  schedule, Cross region copy)
	- AWS System Manager
	- AWS Backup
</details>
<br>
<details><summary> <b>STUDY: Course & Exam Preparation</b></summary>
<br>

### UDEMY

- [AWS Certified DevOps Engineer - Professional 2022](https://www.udemy.com/course/master-aws-certified-devops-engineer-professional/)

- [AWS Certified DevOps Engineer Professional Practice Exams](https://www.udemy.com/course/aws-certified-devops-engineer-professional-practice-exams-s/)

### WHIZLAB

- [aws-devops-certification-training](https://www.whizlabs.com/learn/course/aws-devops-certification-training)

- [AWS Certified DevOps Engineer Professional Practice Tests](https://www.whizlabs.com/learn/course/aws-devops-certification-training/183)

</details>
<br>
<details><summary> <b>INFO: DOP-C01 Exam Breakdown</b></summary>
<br>

### Mark Breakdown

- SDLC Automation (22%)

- Config. Management & IaC (19%)

- Monitoring & Logging (15%)

- Policies & Standard Automation (10%)

- Incident & Event Response (18%)
</details>

