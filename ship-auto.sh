#!/bin/bash

BRANCH=$(git branch --show-current)

echo "🚀 Ship: $BRANCH"

# proteção
if [[ "$BRANCH" != feature/* ]]; then
  echo "❌ Use em feature/*"
  exit 1
fi

# bloqueia se tiver conflito
if git ls-files -u | grep -q .; then
  echo "❌ Existem conflitos. Resolva antes."
  exit 1
fi

# commit (se necessário)
if ! git diff --quiet || ! git diff --staged --quiet; then
  echo "📦 Commitando..."
  git add .
  git commit -m "${1:-update}"
fi

# pull simples (sem rebase)
echo "🔄 Atualizando..."
git pull origin "$BRANCH"

# push
echo "⬆️ Push..."
git push

# PR
echo "📬 PR..."
gh pr create --base developer --head "$BRANCH" --fill || echo "ℹ️ PR já existe"

echo "✅ Done"
echo "🔥 Ship concluído com sucesso!..😎"

#-----------outra-version---------------------

# set -e

# BRANCH=$(git branch --show-current)

# echo "🚀 Ship iniciado na branch: $BRANCH"

# # proteção
# if [[ "$BRANCH" != feature/* ]]; then
#   echo "❌ Use apenas em feature/*"
#   exit 1
# fi

# # verifica mudanças
# if git diff --quiet && git diff --staged --quiet; then
#   echo "⚠️ Nada para commitar"
#   exit 0
# fi

# # sync
# echo "🔄 Sincronizando com remoto..."
# git pull --rebase origin "$BRANCH" || { echo "❌ erro no pull"; exit 1; }

# # 🔥 VALIDAÇÕES INTELIGENTES

# # lint (se existir)
# if npm run | grep -q "lint"; then
#   echo "🧹 Rodando lint..."
#   npm run lint || { echo "❌ erro no lint"; exit 1; }
# else
#   echo "⚠️ lint não configurado — pulando"
# fi

# # test (se existir)
# if npm run | grep -q "test"; then
#   echo "🧪 Rodando testes..."
#   npm test || { echo "❌ testes falharam"; exit 1; }
# else
#   echo "⚠️ testes não configurados — pulando"
# fi

# # audit (não bloqueante)
# echo "🔐 Verificando vulnerabilidades..."
# npm audit --audit-level=high || echo "⚠️ vulnerabilidades encontradas (não bloqueante)"

# # commit
# git add .
# git commit -m "${1:-update}"

# # push
# echo "⬆️ Enviando código..."
# git push || { echo "❌ erro no push"; exit 1; }

# # PR
# if gh pr view "$BRANCH" &>/dev/null; then
#   echo "ℹ️ PR já existe — atualizado"
# else
#   echo "📬 Criando PR..."
#   gh pr create --base developer --head "$BRANCH" --fill
# fi

# echo "✅ Ship concluído com sucesso!"


# 🚀 COMO USAR
# ./ship.sh "feat: login api"
# git ship-auto "feat: login api"

#👉 resultado automático:
# commit ✔
# push ✔
# PR: feature/... → developer ✔

# 🔥 SHIP AJUSTADO
#git config --global alias.ship '!f() { \
#  git add . && \
#  git commit -m "${1:-update}" && \
#  git push && \
#  gh pr create --base developer --head $(git branch --show-current) --fill; \
#}; f'