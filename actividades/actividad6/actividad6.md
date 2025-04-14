# Actividad 6
# Parte 1: git rebase para mantener un historial lineal
### Escenario del ejemplo
![](imagenes/parte1_a.png)
![](imagenes/parte1_b.png)
#### **Tarea**: Realiza el rebase de `new-feature` sobre `main` con los siguientes comandos:
![](imagenes/parte1_c.png)
#### Revisión final:
![](imagenes/parte1_d.png)
# Parte 2: git cherry-pick para la integración selectiva de commit
#### Escenario de ejemplo
![](imagenes/parte2_a.png)
#### **Pregunta:** Muestra un diagrama de como se ven las ramas en este paso.
![](imagenes/parte2_b.png)
##### **Preguntas de discusión:**

1. ¿Por qué se considera que rebase es más útil para mantener un historial de proyecto lineal en comparación con merge?  
	 aaaa
2. ¿Qué problemas potenciales podrían surgir si haces rebase en una rama compartida con otros miembros del equipo?  
	aaaa
3. ¿En qué se diferencia cherry-pick de merge, y en qué situaciones preferirías uno sobre el otro?  
	 aaaa
4. ¿Por qué es importante evitar hacer rebase en ramas públicas?
	 aaaa
#### **Ejercicios teóricos**

1. **Diferencias entre git merge y git rebase**  
   **Pregunta**: Explica la diferencia entre git merge y git rebase y describe en qué escenarios sería más adecuado utilizar cada uno en un equipo de desarrollo ágil que sigue las prácticas de Scrum.
	 dddd

3. **Relación entre git rebase y DevOps**  
   **Pregunta**: ¿Cómo crees que el uso de git rebase ayuda a mejorar las prácticas de DevOps, especialmente en la implementación continua (CI/CD)? Discute los beneficios de mantener un historial lineal en el contexto de una entrega continua de código y la automatización de pipelines.
	 aaaa

5. **Impacto del git cherry-pick en un equipo Scrum**  
   **Pregunta**: Un equipo Scrum ha finalizado un sprint, pero durante la integración final a la rama principal (main) descubren que solo algunos commits específicos de la rama de una funcionalidad deben aplicarse a producción. ¿Cómo podría ayudar git cherry-pick en este caso? Explica los beneficios y posibles complicaciones.
	aaaa

### ejercicios prácticos
#### 1. Simulación de un flujo de trabajo Scrum con git rebase y git merge
![](imagenes/ejercicio1_a.png)
![](imagenes/ejercicio1_b.png)
#### Preguntas:
- **¿Qué sucede con el historial de commits después del rebase?**
Se fusionó el commit **Actualización en main** en la rama principal
![](imagenes/ejercicio1_c.png)
- **¿En qué situación aplicarías una fusión fast-forward en un proyecto ágil?**
Sería muy útil para proyectos en los que la rama principal no avanzó mientras se trabajaba en las ramas generadas.
#### 2. Cherry-pick para integración selectiva en un pipeline CI/CD
![](imagenes/ejercicio2_a.png)
![](imagenes/ejercicio2_b.png)
#### Preguntas:
- **¿Cómo utilizarías cherry-pick en un pipeline de CI/CD para mover solo ciertos cambios listos a producción?**
Usaría cherry-pick para casos en los cuales necesito usar ciertas funciones de otra rama que no hayan estado en el momento en que yo creé mi rama. Otra utilidad que le encuentro es cuando al trabajar sobre una rama encuentro un error que otra persona del equipo ya lo arregló en su rama, asi que podría 
- **¿Qué ventajas ofrece cherry-pick en un flujo de trabajo de DevOps?**
con cherry-pick puedes dar uso de commits hechos en diferentes ramas que pueden ayudar a tener funciones agregadas a la rama donde estás trabajando sin necesidad de colocarse en esa rama y hacer varios merges.
