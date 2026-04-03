#!/bin/bash

for b in mensagem2 mensagem3 mensagem4; do
  echo "Atualizando $b..."
  git checkout $b
  git merge main
done

echo "✔ Todas branches atualizadas...:)"