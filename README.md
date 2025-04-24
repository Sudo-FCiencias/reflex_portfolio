# portafolio.py
Template de portafolio mostrado en el evento "PythonCDMX x Sudo", hecha en Reflex.

# ¿Como instalo las dependencias de la plantilla?

## Siguiendo lo tradicional
Clona el proyecto, crea un entorno virtual, instala Reflex y ejecútalo para acceder al proyecto desde [http://localhost:3000](http://localhost:3000).

```bash
pip install -r requirements.txt"
reflex init
reflex run
```

## La forma rápida
Instala [uv](https://docs.astral.sh/uv/). Clona el repositorio y luego haces lo siguiente
```bash
uv init
uv add -r requirements.txt
source .venv/bin/activate
reflex init
reflex run
```

# ¿Qué debo editar para usar la plantilla?

Si quieres una edición exprés de la plantilla, ve a `assets/data/data.json` o a `assets/data/data(esp).json`
segun sea el idioma en el que necesites el portafolio y editalo con tu información, enlaces, archivos y skills.

En general el mismo archivo te va dando una idea de como debes ir agregando o quitando lo que necesites, ya sea
experiencia laboral, íconos, proyectos, etc. 

Si quieres meterte más hacia lo gráfico, puedes revisar:
- `assets/images/` para cambiar el favicon, las imagenes de tus proyectos, tu avatar, etc.
- `portafolio/styles/styles.py` para hacer ajustes de tamaño.
- `portafolio/portafolio.py` para cambiar el esquema de colores.
- Los iconos generales se corresponden con los identificadores de [Lucide icons](https://lucide.dev/icons/).
- Los iconos de las tecnologías se corresponden con los identificadores de [Devicon](https://devicon.dev/).


## Aviso de Cambio de Idioma

Si deseas usar la plantilla para hacer un portafolio en español, revisa los siguientes archivos para modificar
el texto hardcodeado que aparecerá en algunos lugares de la plantilla (esto no modifica el resto de plantilla)
- Los archivos en `portafolio/views/`
- `index()` en `portafolio/portafolio.py`
- El final de `portafolio/data.py` para cambiar el archivo.


# ¿Cómo lo despliego?

La forma más rápida es usar Vercel. Se configura el despliegue automático desde los archivos [vercel.json](./vercel.json) y [build.sh](./build.sh). Solo debes de conectar tu cuenta de GitHub a la plataforma para poder desplegar los archivos.

# Reconocimientos

Esta plantilla son nuestras modificaciones y documentaciones de la plantilla original de MoureDev. Para ver la plantilla original [haz click aquí.](https://github.com/mouredev/portafolio-template)

# Más Información 
- Para conocer más sobre Reflex y poder leer su documentación [haz click aquí.](https://reflex.dev/)