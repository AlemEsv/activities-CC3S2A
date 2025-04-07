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
