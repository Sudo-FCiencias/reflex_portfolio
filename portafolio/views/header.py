"""
Módulo del header del portafolio.
Incluye el avatar del usuario junto
con a su información de contacto.
"""

import reflex as rx
from portafolio.components.heading import heading
from portafolio.components.media import media
from portafolio.data import Data
from portafolio.styles.styles import Size


def header(data: Data) -> rx.Component:
    """
    Método que genéra el header del portafolio.

    Args:
    ----
        data (Media): Información de tipo Media para ingresar en el header

    Returns:
        rx.Component: HStack con el avatar, aptitudes, ubicación (previstas en data.json)
                      y la información en data.
    """
    return rx.hstack(
        rx.avatar(src=data.avatar, size=Size.BIG.value),
        rx.vstack(
            heading(data.name, True),
            heading(data.skill),
            rx.text(rx.icon("map-pin", color="#66A8E9"), data.location, display="inherit"),
            media(data.media),
            spacing=Size.SMALL.value,
        ),
        spacing=Size.DEFAULT.value,
    )
