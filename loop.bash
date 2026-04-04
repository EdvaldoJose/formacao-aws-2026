#!/bin/bash

for b in developer productiion; do
  echo "Atualizando as branch $b..."
  git checkout $b
  git merge main
done

echo "[✔] Todas as branches foram atualizadas!..:)"