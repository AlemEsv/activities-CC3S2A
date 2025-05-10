#!/usr/bin/env bash

# Activar para robustez
set -euo pipefail

mostrar_ayuda(){
    echo "Uso: $0 [opción]"
    echo "Opciones disponibles:"
    echo "  --branches    Limpiar ramas locales interactivamente"
    echo "  --stashes     Gestionar stashes (aplicar o eliminar)"
    echo "  --backup      Guardar reflog filtrado en archivo"
    echo "  --report      Generar informe JSON del repositorio"
    echo "  --debug       Activar modo de depuración detallado"
    echo "  --help        Mostrar esta ayuda"
}

limpiar_ramas(){
    # Solicitar patrón
    read -rp "Ingresa un patrón para filtrar ramas locales: " patron

    # Validación
    if [[ ! "$patron" =~ ^[[:alnum:]_/.-]+$ ]]; then
    echo "Patrón invalido."
    exit 1
    fi

    echo "Ramas que coinciden con el patrón '$patron':"
    ramas_locales=($(git branch | grep -E "$patron"))

    if [[ ${#ramas_locales[@]} -eq 0 ]]; then
        echo "No hay ramas disponibles."
    else
        for rama in "${ramas_locales[@]}"; do 
            read -rp "¿Eliminar la rama '$rama'? (s/n):  " respuesta
            if [[ $respuesta =~ ^[sS]$ ]]; then
                git branch -D "$rama"
            fi
        done
    fi

    ramas_remotas=($(git branch -r | grep -E "$patron"))

    if [[ ${#ramas_remotas[@]} -eq 0 ]]; then
        echo "No hay ramas disponibles."
    else
        for rama in "${ramas_remotas[@]}"; do 
            read -rp "¿Eliminar la rama '$rama'? (s/n):  " respuesta
            if [[ $respuesta =~ ^[sS]$ ]]; then
                git push origin --delete "$rama"
            fi
        done
    fi

}

gestionar_stashes(){

    # Listar stashes con indices
    stashes=$(git stash list | nl -w2 -s'. ')
    echo "Stashes disponibles:"
    echo "$stashes"

    read -rp "Ingresa los índices de stashes que quieres aplicar: " indices
    read -ra array_indices <<< "$indices"

    for i in "${array_indices[@]}"; do
        if [[ ! $i =~ ^[0-9]+$ ]]; then
            echo "Indice no existente."
            exit 1
        fi

        echo "¿Deseas aplicar o eliminar el stash?"
        echo "1) Aplicar"
        echo "2) Eliminar"
        echo "3) Volver"
        read -rp "Opcion (1/2/3): "opcion

        if [[ $opcion == "1" ]]; then
            git stash apply stash@{$i}
        elif [[ $opcion == "2" ]]; then
            git stash drop stash@{$i}
        elif [[ $opcion == "3" ]]; then
            return
        else
            echo "Opción invalida."
        fi
    done 
}

backup_reflog(){

    #guardar archivo reflog
    archivo="reflog_$(date +%Y%m%d_%H%M%S).log"

    # filtrar reflog con reset o merge
    git reflog | grep -iE 'reset|merge' > "$archivo"

    echo "Reflog filtrado guardado en: $archivo"
}

informe_json(){
    # Obtener datos del repositorio
    rama_actual=$(git rev-parse --abbrev-ref HEAD)
    cantidad_stashes=$(git stash list | wc -l)
    lista_tags=$(git tag | jq -R -s -c 'split("\n")[:-1]')
    submodulos=$(git submodule status | awk '{print $2}' | jq -R -s -c 'split("\n")[:-1]')

    # Construir JSON en variable usando here-document
    json=$(cat <<EOF
{
  "rama_actual": "$rama_actual",
  "cantidad_stashes": $cantidad_stashes,
  "tags": $lista_tags,
  "submodulos": $submodulos
}
EOF
)

    archivo="informe_$(date +%Y%m%d).json"
    # Mostrar el archivo
    echo "$json" | tee "$archivo"
}

case "$1" in
  --branches)
    limpiar_ramas
    ;;
  --stashes)
    gestionar_stashes
    ;;
  --backup)
    backup_reflog
    ;;
  --report)
    informe_json
    ;;
  --debug)
    export PS4='+ ${BASH_SOURCE}:${LINENO}:${FUNCNAME[0]}: '
    set -x
    ;;
  --help|*)
    mostrar_ayuda
    ;;
esac