# Ejercicio de presentación de "mini-proyecto"

Como parte del *aprendizaje práctico, forma equipos y presenten un **"Mini-proyecto de arquitectura en la nube"*:

## 1. Objetivo del sistema:
Se desarrollara una página web que conecta a usuarios (alumnos o estudiantes preuniversitarios) con alumnos universitarios o egresados para recibir una orientacion vocacional. Los usuarios podran registrarse, buscar carreras disponibles, reservar sesiones virtuales, recibir automaticamente una reunion agendada por correo con un enlace de una plataforma de videollamadas, y calificar el servicio recibido

## 2. Selección de modelo de servicio:
Se elegiria PaaS ya que solamente necesito enfocarme en el desarrollo de la pagina web, no de la infrastructura, ademas que me permite desplegar mi web y backend de forma sencilla. Tambien se utilizaria SaaS, ya que se integrara servicios como google meet o Zoom, ademas del Gmail API para el envio automatico de correos.

## 3. Tipo de nube:
Nube pública, nos brinda recursos (servidores, almacenamiento, etc.) ya gestionados por el proveedor externo.
### El proyecto necesita:
- Alta disponibilidad, para que los estudiantes puedan entrar en cualquier
momento.
- Bajos costos, ya que al ser un proyecto muy pequeño no se contará con un
presupuesto.
- Escalabilidad automática para su adaptación dependiendo de la cantidad de
usuarios.
- Mantenimientos mínimos de los servidores, ya que el grupo debe enfocarse en la
lógica del sistema.
### Opciones:
- Heroku: Ideal para novatos y si es que se quiere publicar rápido una API o app
sencilla. Muy amigable.
- Vercel: Perfecto para interfaces en React/Next.js. Es rápido y no se dificulta.
- Supabase: Se usa si se busca un backend robusto con una base de datos real.
Perfecto para apps con un sistema de usuarios.
- Firebase: Perfecto para aplicaciones donde se necesita tiempo real, como chats o
dashboards colaborativos. Tiene todo incluido para frontend y apps móviles.
- Render: Parecido a Heroku, pero nos brinda más control.
### Recomendación:
- Frontend: Vercel + Next.js
- Backend: Supabase, funciones integradas
- Chat/Reuniones: Firebase
- Base de datos: Supabase
- Despliegue: Vercel + Supabase
## 4. Esquema de escalabilidad:
Según las recomendaciones, ya estamos usando servicios en la nube (Vercel, Supabasem
Firebase), ya que se ajustan automáticamente dependiendo de la demanda.
- Vercel: escala automáticamente, si el tráfico es demasiado alto, se puede optar
por planes de pago que nos ayuden.
- Supabase (backend): escala automáticamente, separa funciones críticas y mejora
la eficiencia de las consultas.
- Supabase (base de datos): Escala verticalmente.
- Firebase: Escala sin esfuerzo, si el tráfico es bastante, es recomendable pasar a
Firestore o usar reglas de seguridad eficientes.
- Supabase (autenticación): Se maneja sin complicaciones. Si la demanda es
demasiada, se puede usar proveedores externos, como Google o GitHub, para
balancear cargas.

## 5. Costos (directos o indirectos) y riesgos asociados

### Costos Directos

- **Hosting en la nube:** Se podría usar **Amazon Web Services (AWS)** para alojar la aplicación. Esto incluye EC2 para servidores, RDS para bases de datos y S3 para almacenamiento de archivos.

- **Videollamadas:** Se puede integrar **Twilio Video**, que cobra aproximadamente $0.004 por minuto por participante. Es estable, confiable y permite integración sencilla con la web.

- **Certificados SSL:** Con **Let’s Encrypt** se puede obtener certificados SSL gratuitos, con posibilidad de migrar a certificados de pago si se requieren garantías adicionales.

- **Autenticación:** Con **Firebase Authentication**, base de datos gratuito que permite autenticación con correo, Google, entre otros.

### Costos Indirectos

- **Marketing y adquisición de usuarios:** Habrá inversión en campañas de **Google Ads** y promoción en redes sociales como **Instagram y TikTok**.

- **Soporte técnico:** Se contratará personal para resolver dudas de alumnos y universitarios vía **Zendesk** o correo electrónico.

- **Capacitación a mentores:** Se desarrollarán materiales como videos y guías para los mentores, en conjunto con talleres virtuales via **Google Meet**. El costo será variable, dependiendo del alcance.

- **Moderación de contenido:** Se implementará un sistema de revisión manual y automático de perfiles y calificaciones.

### Riesgos Asociados

- **Poca adopción inicial:** Si no logramos atraer a suficientes usuarios, la plataforma podría parecer vacía y desincentivar su uso. Por lo que se tratará de mitigar con campañas agresivas de difusión y posibles alianzas con diferentes colegios.

- **Malas experiencias:** Un universitario puede dar una mala charla o tener un comportamiento inapropiado, por eso se tiene un sistema de reporte y moderación activa, con posibilidad de expulsión inmediata.

- **Sobrecarga de infraestructura:** Si la plataforma recibe muchos usuarios de golpe, los servidores podrían colapsar. Para evitar esto, se podría hacer un **autoscaling** en AWS y realizar pruebas de carga periódicas.
