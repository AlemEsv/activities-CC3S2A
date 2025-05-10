#!/usr/bin/env bash
# $0,1...n : parametros
# $@: todos los parametros

echo "Script: $0"
echo "1er parámetro: $1"
echo "Todos: $@"
echo "Cantidad: $#"
shift 1
echo "Ahora \$1 es: $1"