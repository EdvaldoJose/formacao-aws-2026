#!/bin/bash

BRANCH=$(git branch --show-current)

# proteção
if [[ "$BRANCH" != feature/* ]]; then
  echo "❌ Use apenas em branch feature/*"
  exit 1
fi

# verifica se há mudanças
if git diff --quiet && git diff --staged --quiet; then
  echo "⚠️ Nada para commitar"
  exit 0
fi

# commit
git add .
git commit -m "${1:-update}"

# push
git push

# verifica se já existe PR
if gh pr view "$BRANCH" &>/dev/null; then
  echo "ℹ️ PR já existe para essa branch"
else
  gh pr create --base developer --head "$BRANCH" --fill
fi

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