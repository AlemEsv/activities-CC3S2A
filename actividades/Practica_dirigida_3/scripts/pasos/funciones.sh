#!/usr/bin/env bash
saludar() {
  local name=$1
  echo "Hola, $name!"
}
saludar "Alem"

dividir() {
  local a=$1 b=$2
  (( b==0 )) && return 1
  echo "$((a/b))"
}
if res=$(dividir 10 2); then
  echo "División: $res"
else
  echo "Error división"
fi