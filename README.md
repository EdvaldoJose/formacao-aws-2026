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

💣 REGRA DE OURO (GRAVA ISSO)
rebase ativo → NÃO muda de branch
rebase ativo → NÃO faz push
rebase ativo → resolve e continua

🔥 FLUXO CORRETO SEMPRE
Antes de qualquer push:
git pull
git push

⚠️ NÃO FAÇA ISSO (PERIGO)
git push --force

🚀 CONFIG GLOBAL (FAZ UMA VEZ)
git config --global pull.rebase false
git config --global rebase.autoStash true
git config --global fetch.prune true
🔥 O QUE ISSO FAZ:
| Config            | Resultado                   |
| ----------------- | --------------------------- |
| pull.rebase false | evita rebase infernal       |
| autoStash true    | salva alterações automático |
| fetch.prune true  | limpa branch morta          |

🚀 FLUXO SEM DOR (DE VERDADE)
🔹 NUNCA MAIS ISSO:
git pull --rebase ❌
git rebase manual ❌
🔹 FAÇA ISSO:
git add .
git commit -m "sua mudança"
git pull
> ou se esqueceu:
git stash
git pull
git stash pop

🚀 EXTRA NÍVEL EMPRESA

Melhor ainda:

👉 você nem trabalha direto na production

feature → PR → merge → acabou

👉 zero conflito local

🔥 RESUMO
Problema	Solução
alteração local	stash ou commit
pull bloqueado	Git protegendo
fluxo limpo	PR + commits pequenos

Faz pull + clean + safe automaticamente 😎
git sync

🔥 VERSÃO MAIS PROFISSIONAL (RECOMENDO)
Essa aqui é mais robusta:
git config --global alias.sync '!git stash push -m "auto-sync" && git pull --no-rebase && git stash pop || true'

💣 POR QUE ESSA É MELHOR

✔ evita rebase
✔ não quebra se não tiver stash
✔ funciona sempre

🚀 EXTRA: LIMPEZA AUTOMÁTICA

Se quiser nível mais alto:
💣 POR QUE ESSA É MELHOR

✔ evita rebase
✔ não quebra se não tiver stash
✔ funciona sempre

🚀 EXTRA: LIMPEZA AUTOMÁTICA

Se quiser nível mais alto:
git config --global alias.cleanall '!git fetch --prune && git branch --merged | grep -v "\*" | xargs -r git branch -d'

git sync     # atualiza seguro
git cleanall # limpa sujeira

💣 VERDADE DIRETA
Você nunca mais deveria rodar:

git pull
👉 use: git sync

criar um comando tipo:
git ship
que:
add
commit
push
abre PR automático

💣 PRÉ-REQUISITO

Instala o CLI do GitHub CLI:

sudo apt install gh -y

Depois autentica:

gh auth login
🚀 1. ALIAS: SHIP (AUTOMAÇÃO TOTAL)
git config --global alias.ship '!f() { \
  git add . && \
  git commit -m "${1:-update}" && \
  git push && \
  gh pr create --fill; \
}; f'

🔥 COMO USAR
git ship "feat: login api"
👉 resultado:
commit criado
push feito
PR aberto automático 🚀

🧠 INTELIGENTE
Se você esquecer a mensagem:
git ship
👉 usa: update

🚀 2. ALIAS: SYNC (SEGURANÇA TOTAL)

(se não criou antes)

git config --global alias.sync '!git stash push -m "auto-sync" && git pull --no-rebase && git stash pop || true'
🚀 3. ALIAS: START (CRIA FEATURE LIMPO)
git config --global alias.start '!f() { \
  git checkout developer && \
  git pull && \
  git switch -c feature/$1; \
}; f'
🔥 USO
git start login-api

👉 cria:

feature/login-api
🚀 4. ALIAS: DONE (FINALIZA)
git config --global alias.done '!git push && gh pr create --fill'
🧠 FLUXO COMPLETO AGORA
git start login-api
# codou...

git ship "feat: login api"

👉 pronto:

PR aberto
CI rodando
fluxo profissional
💣 NÍVEL ABSURDO (OPCIONAL)

Auto PR sempre para developer:

gh pr create --base developer --fill

👉 adapta no alias ship se quiser

🚀 RESULTADO FINAL

Você virou isso:

dev normal: 10 comandos
você:       1 comando
🔥 FILOSOFIA
menos terminal
mais entrega
💣 VERDADE FINAL

Isso aqui é exatamente o que times fazem:

scripts internos
automação de fluxo
PR automático

🚀 COMO USAR
git ship "feat: login api"

👉 resultado automático:
commit ✔
push ✔
PR: feature/... → developer ✔

🔥 SHIP AJUSTADO
git config --global alias.ship '!f() { \
git add . && \
git commit -m "${1:-update}" && \
git push && \
gh pr create --base developer --head $(git branch --show-current) --fill; \
}; f'

✅ CORRETO base: main compare: production 👉 ou seja: production → main

🧠 REGRA compare = (origem) → base = (destino)

🚀 SEQUÊNCIA FINAL CORRETA feature → developer developer → production production → main ✅

Abrindo um PR via terminal: 🔥 PR VIA TERMINAL (RECOMENDADO) gh pr create
--base main
--head production
--title "release: production → main"
--body "Promovendo código validado para produção"

✅ CORRETO
base: main
compare: production
👉 ou seja:
production → main

🧠 REGRA
compare = (origem) → base = (destino)

🚀 SEQUÊNCIA FINAL CORRETA
feature → developer
developer → production
production → main ✅

Abrindo um PR via terminal:
🔥 PR VIA TERMINAL (RECOMENDADO)
gh pr create \
  --base main \
  --head production \
  --title "release: production → main" \
  --body "Promovendo código validado para produção"
  
💣 RESPOSTA
branch atual = feature/login-api

👉 exatamente assim:

git checkout feature/login-api
./clean-feature.sh
🚀 POR QUE ISSO FUNCIONA

Seu script pega automaticamente:

BRANCH=$(git branch --show-current)

👉 então ele precisa que você esteja:

dentro da feature que será deletada
🧠 O QUE ELE FAZ INTERNAMENTE
detecta a branch atual
valida se é feature/*
troca pra developer
deleta a feature

👉 ou seja:

você começa na feature
ele termina fora dela
🚨 SE VOCÊ NÃO ESTIVER NA FEATURE

Exemplo:

git checkout developer
./clean-feature.sh

👉 resultado:

❌ Você não está em uma feature/*

✔ proteção funcionando

🚀 FLUXO CORRETO COMPLETO
# terminou a feature
git checkout feature/login-api

# rodou PR → mergeou

# agora limpa
./clean-feature.sh
💣 DICA PROFISSIONAL

Sempre antes de rodar:

git status

👉 só pra garantir que está na branch certa

🧠 MENTALIDADE
você executa a limpeza de dentro da própria feature
💥 VERDADE FINAL

Esse detalhe simples evita:

deletar branch errada = caos absoluto

🚀 O QUE VOCÊ ACABOU DE FAZER (SEM PERCEBER)

Você rodou um mini pipeline DevOps local:

código → commit → sync → push → PR atualizado → DONE

👉 sem erro
👉 sem conflito
👉 sem dor

💣 O MAIS IMPORTANTE
PR já existe → atualizado automaticamente

👉 isso aqui é nível profissional mesmo

Você não criou PR duplicado
Você não quebrou fluxo
Você só evoluiu o que já estava aberto

🧠 AGORA SEU FLUXO É ESSE (OFICIAL)
🔥 DIA A DIA
git checkout feature/login-api
# faz alteração

./ship-auto.sh "feat: qualquer coisa"
🔥 NO GITHUB
PR → feature → developer
Merge

Depois:

developer → production → main
💥 VERDADE (SEM ROMANTIZAR)

Antes você tava assim:

Git te controlando 😭

Agora:

Você controlando o Git 😎
🚀 PRÓXIMO NÍVEL (SE QUISER)

Agora dá pra subir o nível fácil:

auto merge quando CI passar
proteger main com regra certa
CI rodando em developer e production
deploy automático (AWS no teu caso 👀)

🔥 RESUMO FINAL
✔ script funcionando
✔ fluxo limpo
✔ PR automático
✔ zero dor de cabeca.

🚀 Direto: você deve estar na própria feature/* quando rodar esse script ✅

💣 RESPOSTA
branch atual = feature/login-api

👉 exatamente assim:

git checkout feature/login-api
./clean-feature.sh
🚀 POR QUE ISSO FUNCIONA

Seu script pega automaticamente:

BRANCH=$(git branch --show-current)

👉 então ele precisa que você esteja:

dentro da feature que será deletada
🧠 O QUE ELE FAZ INTERNAMENTE
detecta a branch atual
valida se é feature/*
troca pra developer
deleta a feature

👉 ou seja:

você começa na feature
ele termina fora dela
🚨 SE VOCÊ NÃO ESTIVER NA FEATURE

Exemplo:

git checkout developer
./clean-feature.sh

👉 resultado:

❌ Você não está em uma feature/*

✔ proteção funcionando

🚀 FLUXO CORRETO COMPLETO
# terminou a feature
git checkout feature/login-api

# rodou PR → mergeou

# agora limpa
./clean-feature.sh
💣 DICA PROFISSIONAL

Sempre antes de rodar:

git status

👉 só pra garantir que está na branch certa

🧠 MENTALIDADE
você executa a limpeza de dentro da própria feature
💥 VERDADE FINAL

Esse detalhe simples evita:

deletar branch errada = caos absoluto

🚀 O QUE VOCÊ ACABOU DE FAZER (SEM PERCEBER)

Você rodou um mini pipeline DevOps local:

código → commit → sync → push → PR atualizado → DONE

👉 sem erro
👉 sem conflito
👉 sem dor

💣 O MAIS IMPORTANTE
PR já existe → atualizado automaticamente

👉 isso aqui é nível profissional mesmo

Você não criou PR duplicado
Você não quebrou fluxo
Você só evoluiu o que já estava aberto

🧠 AGORA SEU FLUXO É ESSE (OFICIAL)
🔥 DIA A DIA
git checkout feature/login-api
# faz alteração

./ship-auto.sh "feat: qualquer coisa"
🔥 NO GITHUB
PR → feature → developer
Merge

Depois:

developer → production → main
💥 VERDADE (SEM ROMANTIZAR)

Antes você tava assim:

Git te controlando 😭

Agora:

Você controlando o Git 😎
🚀 PRÓXIMO NÍVEL (SE QUISER)

Agora dá pra subir o nível fácil:

auto merge quando CI passar
proteger main com regra certa
CI rodando em developer e production
deploy automático (AWS no teu caso 👀)

🔥 RESUMO FINAL
✔ script funcionando
✔ fluxo limpo
✔ PR automático
✔ zero dor de cabeca.


🚀 Direto: você deve estar na própria feature/* quando rodar esse script ✅

💣 RESPOSTA
branch atual = feature/login-api

👉 exatamente assim:

git checkout feature/login-api
./clean-feature.sh
🚀 POR QUE ISSO FUNCIONA

Seu script pega automaticamente:

BRANCH=$(git branch --show-current)

👉 então ele precisa que você esteja:

dentro da feature que será deletada
🧠 O QUE ELE FAZ INTERNAMENTE
detecta a branch atual
valida se é feature/*
troca pra developer
deleta a feature

👉 ou seja:

você começa na feature
ele termina fora dela
🚨 SE VOCÊ NÃO ESTIVER NA FEATURE

Exemplo:

git checkout developer
./clean-feature.sh

👉 resultado:

❌ Você não está em uma feature/*

✔ proteção funcionando

🚀 FLUXO CORRETO COMPLETO
# terminou a feature
git checkout feature/login-api

# rodou PR → mergeou

# agora limpa
./clean-feature.sh
💣 DICA PROFISSIONAL

Sempre antes de rodar:

git status

👉 só pra garantir que está na branch certa

🧠 MENTALIDADE
você executa a limpeza de dentro da própria feature
💥 VERDADE FINAL

Esse detalhe simples evita:

deletar branch errada = caos absoluto

🚀 O QUE VOCÊ ACABOU DE FAZER (SEM PERCEBER)

Você rodou um mini pipeline DevOps local:

código → commit → sync → push → PR atualizado → DONE

👉 sem erro
👉 sem conflito
👉 sem dor

💣 O MAIS IMPORTANTE
PR já existe → atualizado automaticamente

👉 isso aqui é nível profissional mesmo

Você não criou PR duplicado
Você não quebrou fluxo
Você só evoluiu o que já estava aberto

🧠 AGORA SEU FLUXO É ESSE (OFICIAL)
🔥 DIA A DIA
git checkout feature/login-api
# faz alteração

./ship-auto.sh "feat: qualquer coisa"
🔥 NO GITHUB
PR → feature → developer
Merge

Depois:

developer → production → main
💥 VERDADE (SEM ROMANTIZAR)

Antes você tava assim:

Git te controlando 😭

Agora:

Você controlando o Git 😎
🚀 PRÓXIMO NÍVEL (SE QUISER)

Agora dá pra subir o nível fácil:

auto merge quando CI passar
proteger main com regra certa
CI rodando em developer e production
deploy automático (AWS no teu caso 👀)

🔥 RESUMO FINAL
✔ script funcionando
✔ fluxo limpo
✔ PR automático
✔ zero dor de cabeca.

🚀 Direto: você deve estar na própria feature/* quando rodar esse script ✅

💣 RESPOSTA
branch atual = feature/login-api

👉 exatamente assim:

git checkout feature/login-api
./clean-feature.sh
🚀 POR QUE ISSO FUNCIONA

Seu script pega automaticamente:

BRANCH=$(git branch --show-current)

👉 então ele precisa que você esteja:

dentro da feature que será deletada
🧠 O QUE ELE FAZ INTERNAMENTE
detecta a branch atual
valida se é feature/*
troca pra developer
deleta a feature

👉 ou seja:

você começa na feature
ele termina fora dela
🚨 SE VOCÊ NÃO ESTIVER NA FEATURE

Exemplo:

git checkout developer
./clean-feature.sh

👉 resultado:

❌ Você não está em uma feature/*

✔ proteção funcionando

🚀 FLUXO CORRETO COMPLETO
# terminou a feature
git checkout feature/login-api

# rodou PR → mergeou

# agora limpa
./clean-feature.sh
💣 DICA PROFISSIONAL

Sempre antes de rodar:

git status

👉 só pra garantir que está na branch certa

🧠 MENTALIDADE
você executa a limpeza de dentro da própria feature
💥 VERDADE FINAL

Esse detalhe simples evita:

deletar branch errada = caos absoluto

🚀 O QUE VOCÊ ACABOU DE FAZER (SEM PERCEBER)

Você rodou um mini pipeline DevOps local:

código → commit → sync → push → PR atualizado → DONE

👉 sem erro
👉 sem conflito
👉 sem dor

💣 O MAIS IMPORTANTE
PR já existe → atualizado automaticamente

👉 isso aqui é nível profissional mesmo

Você não criou PR duplicado
Você não quebrou fluxo
Você só evoluiu o que já estava aberto

🧠 AGORA SEU FLUXO É ESSE (OFICIAL)
🔥 DIA A DIA
git checkout feature/login-api
# faz alteração

./ship-auto.sh "feat: qualquer coisa"
🔥 NO GITHUB
PR → feature → developer
Merge

Depois:

developer → production → main
💥 VERDADE (SEM ROMANTIZAR)

Antes você tava assim:

Git te controlando 😭

Agora:

Você controlando o Git 😎
🚀 PRÓXIMO NÍVEL (SE QUISER)

Agora dá pra subir o nível fácil:

auto merge quando CI passar
proteger main com regra certa
CI rodando em developer e production
deploy automático (AWS no teu caso 👀)

🔥 RESUMO FINAL
✔ script funcionando
✔ fluxo limpo
✔ PR automático
✔ zero dor de cabeca.
