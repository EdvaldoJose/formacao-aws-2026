#!/bin/bash

<<<<<<< HEAD
# Lista de branches para atualizar
branches=("developer" "production")

for b in "${branches[@]}"; do
  echo "Atualizando a branch $b..."

  # Tenta mudar de branch, se falhar ele para o script
  git checkout $b || exit 1

  # Tenta mesclar a main
  if git merge main --no-edit; then
    echo " [✔] $b atualizada com sucesso."
  else
    echo " [✘] Erro de conflito na branch $b. Resolva manualmente."
    exit 1
  fi
done

# Volta para a main ao finalizar
git checkout main

echo "++++++++++++++"
echo "[✔] Todas as branches foram atualizadas!..:)"
echo "[✔] main > [✔] developer > [✔] production"
=======
for b in developer production; do
  echo "Atualizando as branch $b..."
  git checkout $b
  git merge main
done
echo "++++++++++++++"
echo "[✔] Todas as branches foram atualizadas!..:)"
echo "[✔] main > [✔] developer > [✔] production"

