# portafolio.py
Template de portafolio mostrado en el evento "PythonCDMX x Sudo" @ Facultad de Ciencias, UNAM, el 25 de Abril de 2025 hecha en Reflex.
Update: Y también mostrada en el webinar "Python 360°: De la Web a la Ciencia de Datos" el 25 de de Noviembre de 2025.

# ¿Como instalo las dependencias de la plantilla?

## Siguiendo lo tradicional

Clona el proyecto, instala Python, crea un entorno virtual, instala Reflex y ejecútalo para acceder al proyecto desde [el puerto 300](http://localhost:3000).

```bash
pip install -r requirements.txt"
reflex init
reflex run
```

## La forma rápida

Instala [uv](https://docs.astral.sh/uv/). Clona el repositorio y luego haces lo siguiente

```bash
uv init
source .venv/bin/activate
uv add -r requirements.txt
reflex init
reflex run
```

Esto abrirá [el puerto 300](http://localhost:3000) para accedas desde tu navegador y puedas visualizar tus cambios.

# ¿Qué debo editar para usar la plantilla?

Si quieres una edición exprés de la plantilla, ve a `assets/data/data.json` o a `assets/data/data(esp).json`
segun sea el idioma en el que necesites el portafolio y editalo con tu información, enlaces, archivos y skills.

En general el mismo archivo te va dando una idea de como debes ir agregando o quitando lo que necesites, ya sea
experiencia laboral, íconos, proyectos, etc. 

Si quieres meterte más hacia lo gráfico, puedes revisar:
- `assets/images/` para cambiar el favicon, las imagenes de tus proyectos, tu avatar, etc.
- `portafolio/styles/styles.py` para hacer ajustes de tamaño.
- `portafolio/portafolio.py` para cambiar el esquema de colores.
- Los iconos generales corresponden con los identificadores de [Lucide icons](https://lucide.dev/icons/).
- Los iconos de las tecnologías corresponden con los identificadores de [Devicon](https://devicon.dev/).

## Aviso de Cambio de Idioma

Si deseas usar la plantilla para hacer un portafolio en español, revisa los siguientes archivos para modificar
el texto hardcodeado que aparecerá en algunos lugares de la plantilla (esto no modifica el resto de plantilla)
- Los archivos en `portafolio/views/`
- `index()` en `portafolio/portafolio.py`
- El final de `portafolio/data.py` para cambiar el archivo.

# ¿Cómo lo despliego?

La forma más rápida es usar [Vercel](https://vercel.com/). Se configura el despliegue automático desde los archivos [vercel.json](./vercel.json) y [build.sh](./build.sh). Solo debes de conectar tu cuenta de GitHub y el repo a Vercel para poder desplegar los archivos. Para obtener un dominio más _profesional_ puedes usar [is-a.dev](https://is-a.dev/) y hacer los ajustes necesarios para conectar tu dominio.

# Reconocimientos

Esta plantilla son nuestras modificaciones y documentaciones de la plantilla original de MoureDev. Para ver la plantilla original [haz click aquí.](https://github.com/mouredev/portafolio-template)

# Más Información 
- Para conocer más sobre Reflex y poder leer su documentación [haz click aquí.](https://reflex.dev/)
