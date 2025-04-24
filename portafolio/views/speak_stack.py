"""
Generador de las badges de los idiomas a incluir en el portafolio.
Es igual a tech_stack, pero sin considerar íconos.
"""

import reflex as rx
from portafolio.components.heading import heading
from portafolio.data import Language
from portafolio.styles.styles import Size


def speak_stack(languages: list[Language]) -> rx.Component:
    """

    Método para generar las badges de los idiomas ingresados
    al portafolio.

    Args
    ----
        languages (list[Language]): Lista de tipo Language (la clase)

    Returns
    -------
         rx.Component: vstack con las badges creadas para languages.
    """
    return rx.vstack(
        # Recuerda cambiar de idioma esta parte
        heading("Languages I Speak"),
        rx.flex(
            *[rx.badge(rx.text(technology.name), size="3") for technology in languages],
            wrap="wrap",
            spacing=Size.SMALL.value,
        ),
        spacing=Size.DEFAULT.value,
    )
