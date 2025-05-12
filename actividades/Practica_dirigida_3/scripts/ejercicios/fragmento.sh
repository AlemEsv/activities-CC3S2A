#!/usr/bin/env bash

salida="salida.txt"
error="errores.txt"

ejecuciones=0

while true; do 
    ejecuciones=$((ejecuciones + 1))
    ./aleatorio.sh >> "$salida" 2>> "$error"

    # cuando no es 0 retorne un error
    if [[ $? -ne 0 ]]; then
        echo "El script falló luego de $ejecuciones ejecuciones"
        break
    fi
done