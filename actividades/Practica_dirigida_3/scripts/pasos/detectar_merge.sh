git log --grep='^Merge branch' --pretty=format:'%s' | \
  grep -Po '(?<=Merge branch )'[^']+' 
# Captura el nombre de la rama tras "merge branch '<rama>'"