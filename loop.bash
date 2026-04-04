#!/bin/bash

for b in developer production; do
  echo "Atualizando as branch $b..."
  git checkout $b
  git merge main
done
echo "++++++++++++++"
echo "[✔] Todas as branches foram atualizadas!..:)"
echo "[✔] main > [✔] developer > [✔] production"
