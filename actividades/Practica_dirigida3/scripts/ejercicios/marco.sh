#!/usr/bin/env bash
marco(){
    # variable global
    export MARCO_DIR="$PWD"
    echo "Estás en el directorio: $MARCO_DIR"
}

polo(){
    cd "$MARCO_DIR"
    echo "Se retornó al directorio: $MARCO_DIR"
}