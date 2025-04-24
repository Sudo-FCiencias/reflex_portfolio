"""

Generador de las badges de las tecnologías a incluir en el portafolio.
Estas se unen en un vstack donde c/u tiene un nombre y el ícono a usar.

"""

import reflex as rx
from portafolio.components.heading import heading
from portafolio.data import Technology
from portafolio.styles.styles import Size


def tech_stack(technologies: list[Technology]) -> rx.Component:
    """

    Método para generar las badges de las tecnologías ingresadas
    al portafolio.

    Args
    ----
        technologies (list[Technology]): Lista de tipo Tecnology (la clase)

    Returns
    -------
        rx.Component: vstack con las badges creadas para technologies.
    """
    return rx.vstack(
        heading("Technologies & Programming Languages I Use"),
        rx.flex(
            *[
                rx.badge(
                    rx.box(
                        class_name=technology.icon,
                        font_size="22px",
                        padding_x="4px",
                        padding_y="4px",
                    ),
                    rx.text(technology.name),
                    size="3",
                )
                for technology in technologies
            ],
            wrap="wrap",
            spacing=Size.SMALL.value,
        ),
        spacing=Size.DEFAULT.value,
    )
