"""
Configuración de los headings del portafolio.
"""

import reflex as rx
from portafolio.styles.styles import Size


def heading(text: str, h1=False) -> rx.Component:
    """
    Método para generar un heading con configuración
    específica.

    Args
    ----
        text (str): Texto a incluir en el heading.
        h1 (bool, optional): Tamaño del heading. H1 por default (False), H2 en caso contrario..

    Returns
    -------
        rx.Component: _description_
    """
    return rx.heading(
        text, as_="h1" if h1 else "h2", size=Size.BIG.value if h1 else Size.MEDIUM.value
    )
