# listado de archivos y guardado
ls -l > listado.txt
# Busqueda de f1 en logs y guardado
grep f1 *.log 2> errores.log
# ambos
make &> build.log
# pipe
# lista, filtra y extrae el segundo campo de los procesos
ps aux | grep sshd | awk '{print $2}'
# sustitución
# sort: ordena archivos
diff <(sort file1) <(sort file2)