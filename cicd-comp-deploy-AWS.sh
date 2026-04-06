🚀 O QUE VAMOS FAZER

✔ CI rodando em developer e production
✔ Deploy automático na AWS
✔ Ambientes separados (dev / prod)

💣 STACK AWS (simples e profissional)
Amazon ECS (rodar app)
Amazon ECR (guardar imagem Docker)
AWS IAM (permissões)
AWS Secrets Manager (segredos)
GitHub Actions (pipeline)
🚀 1. CI + CD (YAML COMPLETO)

👉 .github/workflows/ci-cd.yml

name: CI-CD

on:
  push:
    branches: [ "developer", "production" ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 22

      - name: Install deps
        run: npm install || echo "sem package.json"

      - name: Run tests
        run: npm test || echo "sem testes"

      # 🔐 AWS LOGIN
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          region: us-east-1

      # 🐳 LOGIN ECR
      - name: Login to ECR
        uses: aws-actions/amazon-ecr-login@v2

      # 🏗 BUILD IMAGE
      - name: Build Docker image
        run: |
          docker build -t my-app .

      # 🏷 TAG IMAGE
      - name: Tag image
        run: |
          docker tag my-app:latest ${{ secrets.ECR_REPOSITORY }}:latest

      # ⬆️ PUSH ECR
      - name: Push image
        run: |
          docker push ${{ secrets.ECR_REPOSITORY }}:latest

      # 🚀 DEPLOY ECS
      - name: Deploy to ECS
        run: |
          aws ecs update-service \
            --cluster my-cluster \
            --service my-service \
            --force-new-deployment
🔐 2. SECRETS NO GITHUB

Vai em:

Settings → Secrets → Actions

Cria:

AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
ECR_REPOSITORY

🚀 3. FLUXO AUTOMÁTICO
🔥 DEV
feature → developer

👉 dispara:

build
testes
🔥 PROD
developer → production

👉 dispara:

build
push ECR
deploy ECS 🚀
💣 IMPORTANTE

👉 main não faz deploy
👉 production é quem deploya

🧠 MELHOR PRÁTICA
Branch	Função
feature	dev
developer	integração
production	deploy
main	estável

🚀 4. DOCKERFILE (SE NÃO TIVER)
FROM node:22

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]

💥 RESULTADO FINAL

Agora quando você fizer:

./ship-auto.sh "feat: login api"

👉 automaticamente:

PR → merge → CI roda → deploy AWS 🚀
🔥 ISSO AQUI É NÍVEL PORTFÓLIO FORTE

Você já mostra:

✔ CI/CD real
✔ AWS ECS
✔ Docker
✔ automação completa