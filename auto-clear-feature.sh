#!/bin/bash

BRANCH=$(git branch --show-current)

echo "👉 Branch atual: $BRANCH"

# proteção
if [[ "$BRANCH" != feature/* ]]; then
  echo "❌ Você não está em uma feature/*"
  exit 1
fi

# verifica se já foi mergeada
if git branch --merged | grep -q "$BRANCH"; then
  echo "✅ Branch já foi mergeada. Pode deletar.🚀"
else
  echo "👉 Branch ainda NÃO foi mergeada!⚠️"
  read -p "Deseja apagar mesmo assim? (y/N): " confirm
  [[ "$confirm" != "y" ]] && exit 1
fi

# muda para developer antes de deletar
git checkout developer

# deleta local
git branch -d "$BRANCH"

# deleta remoto
git push origin --delete "$BRANCH"

echo "💀 Branch $BRANCH removida com sucesso!🔥"
