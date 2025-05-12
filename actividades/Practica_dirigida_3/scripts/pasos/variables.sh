#!/usr/bin/env bash
nombre="Alem"
readonly PI=3.14159
export env="producción"

set -u
echo "Usuario: $nombre"
echo "PI value: $PI"
echo "Entorno: $env"