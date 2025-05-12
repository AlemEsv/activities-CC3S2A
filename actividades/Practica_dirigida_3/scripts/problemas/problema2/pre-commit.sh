#!/usr/bin/env bash

set -euo pipefail

check_todo_comments(){
    has_errors=false
    archivos_staged=$(git diff --cached --name-only --diff-filter=ACM)

    for archivo in "${archivos_staged[@]}"; do
        while IFS= read -r linea; do
            errores+=("[$archivo] $linea")
            has_errors=true
        done < <(grep -En 'TODO|FIXME' "$archivo" || true)
    done

}

run_shellcheck() {
    for file in "${staged_files[@]}"; do
        [[ "$file" == *.sh ]] || continue
        output=$(shellcheck "$file" 2>&1) || {
            errors+=("ShellCheck - $file:\n$output")
            has_errors=true
        }
    done
}

run_pyflakes() {
    for file in "${staged_files[@]}"; do
        [[ "$file" == *.py ]] || continue
        output=$(pyflakes "$file" 2>&1)
        if [[ -n "$output" ]]; then
            errors+=("Pyflakes - $file:\n$output")
            has_errors=true
        fi
    done
}

generar_reporte() {
    timestamp=$(date +%Y%m%d_%H%M%S)
    archivo="precommit_report_$timestamp.txt"
    {
        echo "Rama: $(git rev-parse --abbrev-ref HEAD)"
        echo ""
        echo "Archivos staged:"
        printf '%s\n' "${staged_files[@]}"
        echo ""
        echo "git status --short:"
        git status --short
        echo ""
        echo "Errores:"
        printf '%s\n\n' "${errors[@]}"
    } > "$archivo"
    
    echo "Reporte generado en $archivo"
}


errores=()
has_errors=false
archivos_staged=()

check_todo_comments
run_shellcheck
run_pyflakes

if [[ "$has_errors" == true ]]; then
    echo "Se encontraron problemas:"
    printf '%s\n' "${errores[@]}"
    generar_reporte
    exit 1
else
    echo "Todo limpio."
fi