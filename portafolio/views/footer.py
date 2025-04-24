"""
Módulo del footer del portafolio.
En resumidas cuentas es una copia de header,
pero incluye un header para un "call for action".
"""

import reflex as rx
from portafolio.components.media import media
from portafolio.data import Media
from portafolio.styles.styles import Size


def footer(data: Media) -> rx.Component:
    """
    Método que genéra el footer del portafolio.

    Args:
    ----
        data (Media): Información de tipo Media para ingresar en el footer

    Returns:
        rx.Component: HStack con el "Call to Action" y la información en data.
    """
    return rx.hstack(rx.heading("Let's Get in Touch"), media(data), spacing=Size.BIG.value)
