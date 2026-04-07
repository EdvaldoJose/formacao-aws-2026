🧠 ARQUITETURA FINAL (PRO)
GitHub Actions → ECR → ECS Fargate → ALB → Internet
                         ↓
                       VPC
🚀 STACK
Amazon ECS (Fargate)
Amazon ECR
Application Load Balancer
Amazon VPC
Terraform
📁 ESTRUTURA
infra/
 ├── main.tf
 ├── variables.tf
 ├── outputs.tf
 ├── vpc.tf
 ├── ecs.tf
 ├── ecr.tf
 ├── alb.tf
🚀 1. PROVIDER
main.tf
provider "aws" {
  region = "us-east-1"
}

terraform {
  required_version = ">= 1.5"
}
🌐 2. VPC
vpc.tf
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "public" {
  count = 2
  vpc_id = aws_vpc.main.id
  cidr_block = "10.0.${count.index}.0/24"
  map_public_ip_on_launch = true
}
🐳 3. ECR
ecr.tf
resource "aws_ecr_repository" "app" {
  name = "my-app"
}
⚖️ 4. ALB
alb.tf
resource "aws_lb" "app" {
  name               = "app-lb"
  internal           = false
  load_balancer_type = "application"
  subnets            = aws_subnet.public[*].id
}

resource "aws_lb_target_group" "app" {
  name     = "app-tg"
  port     = 3000
  protocol = "HTTP"
  vpc_id   = aws_vpc.main.id
}

resource "aws_lb_listener" "app" {
  load_balancer_arn = aws_lb.app.arn
  port              = 80

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.app.arn
  }
}
🚀 5. ECS + FARGATE
ecs.tf
resource "aws_ecs_cluster" "main" {
  name = "app-cluster"
}

resource "aws_ecs_task_definition" "app" {
  family                   = "app-task"
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  cpu                      = "256"
  memory                   = "512"

  container_definitions = jsonencode([
    {
      name  = "app"
      image = "${aws_ecr_repository.app.repository_url}:latest"
      portMappings = [{
        containerPort = 3000
      }]
    }
  ])
}

resource "aws_ecs_service" "app" {
  name            = "app-service"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.app.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets = aws_subnet.public[*].id
    assign_public_ip = true
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.app.arn
    container_name   = "app"
    container_port   = 3000
  }
}
🚀 6. OUTPUT
outputs.tf
output "url" {
  value = aws_lb.app.dns_name
}
🚀 7. EXECUÇÃO
terraform init
terraform plan
terraform apply
💣 RESULTADO

Você vai ter:

✔ ECS rodando container
✔ ALB com URL pública
✔ deploy automático via CI

🚀 INTEGRAÇÃO COM SEU CI

No seu pipeline:

docker build -t my-app .
docker tag my-app:latest <ECR_URL>:latest
docker push <ECR_URL>:latest

aws ecs update-service \
  --cluster app-cluster \
  --service app-service \
  --force-new-deployment
🧠 EVOLUÇÃO PROFISSIONAL

Depois disso você pode subir pra:

Terraform modules
Remote state (S3 + DynamoDB)
Blue/Green deploy
Auto Scaling
Observabilidade com CloudWatch
💥 VERDADE

Agora você saiu de:

script local

pra:

infra cloud automatizada de verdade