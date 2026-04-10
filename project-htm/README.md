Criando fluxo para colocar projeto na nuvem AWS.

🚀 1. CRIAR O CLUSTER Amazon EKS
🔹 Mais simples (rápido pra testar)
eksctl create cluster \
  --name devops-cluster \
  --region us-east-1 \
  --nodegroup-name workers \
  --node-type t3.small \
  --nodes 1

⏳ demora ~15 min

🔗 Configurar acesso
aws eks update-kubeconfig --region us-east-1 --name devops-cluster

Testa:

kubectl get nodes
🐳 2. BUILD DA IMAGEM (seu Nginx)

Dentro do projeto:

docker build -t meu-site-nginx .

Testa local (opcional):

docker run -p 8081:80 meu-site-nginx
☁️ 3. CRIAR E LOGAR NO ECR
🔹 Criar repositório
aws ecr create-repository \
  --repository-name meu-site-nginx \
  --region us-east-1
🔐 Login
aws ecr get-login-password --region us-east-1 | \
docker login --username AWS --password-stdin <SEU_ECR_URL>
🏷️ Tag da imagem
docker tag meu-site-nginx:latest <SEU_ECR_URL>:v1
🚀 Push
docker push <SEU_ECR_URL>:v1

👉 Agora sua imagem está na AWS

🚀 4. INSTALAR Argo CD
kubectl create namespace argocd
kubectl apply -n argocd \
-f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
🔑 Pegar senha
kubectl get secret argocd-initial-admin-secret \
-n argocd -o jsonpath="{.data.password}" | base64 -d
🌐 Acessar UI
kubectl port-forward svc/argocd-server -n argocd 8080:443

Abre:

https://localhost:8080

Login:

user: admin
senha: (comando acima)
📁 5. CRIAR GITOPS REPO (GitHub)

Cria repo: gitops-repo

Estrutura:

gitops-repo/
└── k8s/
    ├── deployment.yaml
    └── service.yaml
🔹 deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: meu-site
spec:
  replicas: 1
  selector:
    matchLabels:
      app: meu-site
  template:
    metadata:
      labels:
        app: meu-site
    spec:
      containers:
        - name: meu-site
          image: <SEU_ECR_URL>:v1
          ports:
            - containerPort: 80
🔹 service.yaml
apiVersion: v1
kind: Service
metadata:
  name: meu-site-service
spec:
  type: LoadBalancer
  selector:
    app: meu-site
  ports:
    - port: 80
      targetPort: 80
🔼 Subir repo
git init
git add .
git commit -m "initial gitops config"
git remote add origin https://github.com/SEU_USER/gitops-repo.git
git push -u origin main
🔗 6. CONECTAR REPO NO ARGOCD

Instala CLI (opcional):

brew install argocd

Criar app:

argocd app create meu-site \
  --repo https://github.com/SEU_USER/gitops-repo.git \
  --path k8s \
  --dest-server https://kubernetes.default.svc \
  --dest-namespace default
▶️ Sincronizar
argocd app sync meu-site
🌐 7. ACESSAR SUA APP NO EKS
kubectl get svc

Procura:

meu-site-service   LoadBalancer   EXTERNAL-IP

Acessa:

http://EXTERNAL-IP
🔁 8. TESTE FINAL (O FLUXO COMPLETO)
🔥 Nova versão
docker build -t meu-site-nginx .
docker tag meu-site-nginx:latest <ECR>:v2
docker push <ECR>:v2
🔥 Atualiza GitOps
image: <ECR>:v2
🔥 Commit
git commit -am "update image"
git push
💥 Resultado
Argo CD detecta mudança
Deploy automático no Amazon EKS
Sem mexer no cluster
💸 IMPORTANTE (CUSTO)

👉 EKS NÃO é free

Pra economizar:

eksctl delete cluster --name devops-cluster

ou

terraform destroy
🎯 O QUE VOCÊ ACABOU DE FAZER

Você montou:

✔ Build de container
✔ Registry (ECR)
✔ Cluster Kubernetes
✔ Deploy automático
✔ GitOps real

🔥 AGORA SIM — NÍVEL INTERNACIONAL

Você pode falar:

“I implemented a full GitOps workflow deploying containerized applications to EKS using ArgoCD and ECR”

👉 Isso passa em filtro de recrutador gringo.

Se quiser, próximo passo eu te entrego:

👉 CI/CD automático (sem build manual)
👉 Helm + versionamento semântico
👉 Domínio + HTTPS (CloudFront + Route53)

Aí você não só passa… você escolhe vaga.