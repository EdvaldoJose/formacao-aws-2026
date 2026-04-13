aws ecr create-repository \
  --repository-name meu-site-nginx \
  --region us-east-1
#aws ecr get-login-password \
#  --region us-east-1 | docker login \
#  --username AWS \
#  --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com
#docker build -t meu-site-nginx .
#docker tag meu-site-nginx:latest 123456789012.dkr.ecr.us-east-1.amazonaws.com/meu-site-nginx:latest
#docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/meu-site-nginx:latest
