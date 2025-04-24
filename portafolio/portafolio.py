"""
Crea la WebApp del portafolio.

Funciones:
    - index() -> Crea la página principal de la WebApp.

"""

import reflex as rx
from portafolio import data
from portafolio.styles.styles import BASE_STYLE, MAX_WIDTH, STYLESHEETS, EmSize, Size
from portafolio.views.about import about
from portafolio.views.footer import footer
from portafolio.views.header import header
from portafolio.views.info import info
from portafolio.views.tech_stack import tech_stack
from portafolio.views.speak_stack import speak_stack
from portafolio.views.color_toggle import color_toggle
from portafolio.views.extra import extra

DATA = data.data


def index() -> rx.Component:
    """
    Página principal del portafolio. El nombre index corresponde
    a la norma de que la página inicial sea nombrada "index".

    Returns
    -------
        rx.Component: Componente de Reflex con la información del portafolio.
    """
    return rx.center(
        rx.vstack(
            color_toggle(),
            header(DATA),
            about(DATA.about),
            rx.divider(),
            tech_stack(DATA.technologies),
            rx.divider(),
            speak_stack(DATA.languages),
            rx.divider(),
            info("Education & Certifications", DATA.training),
            rx.divider(),
            info("Experience", DATA.experience),
            rx.divider(),
            info("Projects", DATA.projects),
            # Descomenta esto si necesitas agregar algo extra. Guiate del formato en data.json
            # extra(DATA.extras),
            rx.divider(),
            footer(DATA.media),
            spacing=Size.MEDIUM.value,
            padding_x=EmSize.MEDIUM.value,
            padding_y=EmSize.BIG.value,
            max_width=MAX_WIDTH,
            width="100%",
        )
    )


app = rx.App(
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,
    theme=rx.theme(
        appearance="dark",
        accent_color="blue",
        radius="full",
        panel_background="solid",
        scaling="100%",
    ),
)

title = DATA.title
description = DATA.description
image = DATA.image

app.add_page(
    index,
    title=title,
    description=description,
    image=image,
    meta=[
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": image},
    ],
)
