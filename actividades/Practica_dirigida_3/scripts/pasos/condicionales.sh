#!/usr/bin/env bash
num=$1
# [[-z]]: verifica si la cadena está vacia
if [[ -z $num ]]; then
  echo "Pasa un número"
  exit 1
elif (( num % 2 == 0 )); then
  echo "$num es par"
else
  echo "$num es impar"
fi

exit="$2"
case "$exit" in
  txt) echo "Texto" ;;
  sh)  echo "Shell" ;;
  py)  echo "Python" ;;
  *)   echo "Desconocido" ;;
esac