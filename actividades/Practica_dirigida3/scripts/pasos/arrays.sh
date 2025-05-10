#!/usr/bin/env bash

FRUTAS=(manzana banana cereza)
FRUTAS+=("durazno")
echo "Total frutas: ${#FRUTAS[@]}"
for f in "${FRUTAS[@]}"; do
  echo "Fruta: $f"
done
# array de 2 items
declare -A EDADES=([Alice]=28 [Alem]=21)
echo "Alem tiene ${EDADES[Alem]} años"