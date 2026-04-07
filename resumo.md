🧠 1. O QUE É gh (GitHub CLI)

gh é o terminal do GitHub.

👉 você faz no terminal o que faria no site:

gh pr create
gh pr list
gh repo clone
gh auth login

👉 no seu fluxo:

ship-auto → cria PR automático via gh

💥 resumo:

gh = automatizar GitHub sem abrir o browser
🔐 AUTENTICAÇÃO NO GITHUB (IMPORTANTE)

Você precisa logar no gh:

gh auth login

👉 isso cria um token seguro

Sem isso:

PR não cria
push pode falhar
automação quebra

💥 resumo:

auth = permitir que seu script fale com o GitHub
⚠️ 2. O QUE É REBASE (A TRETA)

Rebase = reescrever histórico

👉 exemplo:

A---B---C (main)
     \
      D---E (feature)

Rebase faz:

A---B---C---D'---E'

👉 ele “move” seus commits

💣 PROBLEMA DO REBASE
gera conflito fácil
bagunça histórico
quebra fluxo se não souber usar
🧠 RESUMO HONESTO
rebase = poderoso, mas perigoso
merge = simples e seguro

👉 no seu caso:

EVITA rebase
🚀 3. O QUE É CI (Continuous Integration)

CI = rodar validação automática quando você sobe código

👉 exemplo:

git push → CI roda

CI faz:

build
testes
lint
validação
💥 EXEMPLO REAL (SEU CASO)

No seu .yml:

on:
  push:
    branches: [developer, production]

👉 quando você faz push:

GitHub Actions roda automaticamente
🧠 RESUMO
CI = robô que valida seu código antes de ir pra frente
🚀 AGORA OS NÍVEIS QUE VOCÊ PEDIU
🔥 “quero isso como padrão de equipe”

👉 padrão profissional:

feature/* → developer → production → main

✔ ninguém mexe direto na main
✔ tudo passa por PR
✔ CI valida tudo

🔥 “quero fluxo blindado sem erro humano”

👉 regras:

bloquear push direto na main
obrigar PR
exigir CI passar

💥 resultado:

dev não quebra produção
🔥 “quero PR automático com padrão profissional”

👉 você já tem:

./ship-auto.sh "feat: algo"

isso faz:

commit → push → PR automático
🔥 “quero CI/CD completo com limpeza + deploy automático”

👉 fluxo completo:

ship-auto
   ↓
PR
   ↓
merge developer
   ↓
CI roda
   ↓
merge production
   ↓
deploy AWS 🚀
🔥 “quero clean inteligente com GitHub integrado”

👉 você já começou:

script limpa commit
evita PR duplicado
sincroniza branch

e pode evoluir pra:

deletar branch automaticamente
atualizar PR sozinho
evitar conflitos comuns
💣 RESUMO FINAL (SEM ENROLAÇÃO)
Conceito	O que é
gh	CLI do GitHub
auth	login para automação
rebase	reescreve histórico (perigoso)
CI	valida código automaticamente
🚀 O QUE VOCÊ TEM AGORA
✔ fluxo profissional
✔ PR automático
✔ CI rodando
✔ base pra deploy AWS
🔥 VERDADE FINAL

Você saiu de:

git manual bagunçado 😭

pra:

pipeline automatizado estilo empresa 😎
