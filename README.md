# Curso Formacao AWS 2026.
### Laboratorio: Abril (x) > Laboratorio: Maio (...)
### Laboratorio: Junho (...) > Laboratorio: Julho (...) 
### Laboratorio: Agosto (...) > Laboratorio: Setembro (...) 
### Laboratorio: Outubro (...) > Laboratorio: Novembro (...) 
##### Duracao do Curso: Maio 2026 / Maio 2027.

| Branch     | Papel           |
| ---------- | --------------- |
| feature    | desenvolvimento |
| developer  | integração      |
| production | validação       |
| main       | produção        |

🧠 POR QUE usar feature/*?
Sem isso:
você quebra developer
mistura código incompleto
dificulta rollback
Com isso:
trabalha isolado
faz PR limpo
CI valida tudo

👉 é padrão de empresa (Git Flow simplificado)

🧨 RESUMO
| Etapa     | Fluxo                  |
| --------- | ---------------------- |
| dev       | feature → developer    |
| validação | developer → production |
| produção  | production → main      |

🧠 REGRA SIMPLES
main = destino final
feature/* → developer → production → main

feature/login-api
   ↓ CI
developer
   ↓ CI
production
   ↓ CD (staging)
main
   ↓ DEPLOY 🚀 (AWS)

🔥 BENEFÍCIO REAL
> não quebra produção
> rollback fácil
> deploy controlado
> pipeline automático

👉 volta a main pro estado anterior
git switch main
git reset --hard origin/main

💣 SITUAÇÃO

Você já fez:
✔ alterou na developer
✔ commitou
✔ deu push

👉 agora quer subir isso até a main

🚀 PASSO A PASSO CORRETO
🔹 1. developer → production
👉 No GitHub:
Vai no repo
Clica em Pull requests
New Pull Request
👉 Configura:
base: production
compare: developer
👉 Depois:
cria PR
verifica CI (tem que estar verde ✅)
clica em Merge
🔥 Resultado:

👉 agora production tem as mudanças da developer

🔹 2. production → main

Repete o processo:

👉 New Pull Request:
base: main
compare: production
👉 Depois:
verifica CI
merge
🔥 Resultado final:

👉 main atualizada com segurança 🚀

⚠️ IMPORTANTE

👉 você NÃO faz isso:

git checkout production
git merge developer

👉 isso quebra o fluxo que você acabou de montar

🧠 FLUXO VISUAL
developer
   ↓ PR
production
   ↓ PR
main 🚀
💣 DICA (EVITA PROBLEMA)

Antes de abrir PR:

git switch developer
git pull

👉 garante que está atualizado

⚡ SE DER CONFLITO

GitHub vai avisar:
👉 “This branch has conflicts”

Você resolve assim:
git switch production
git pull
git merge developer
# resolve conflito
git add .
git commit -m "fix: resolve conflito"
git push

| Etapa         | Ação |
| ------------- | ---- |
| dev → prod    | PR   |
| prod → main   | PR   |
| validação     | CI   |
| deploy futuro | main |
<<<<<<< HEAD
seu conteúdo
=======
conteúdo remoto
>>>>>>> 
