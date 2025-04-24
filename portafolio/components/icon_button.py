"""
Configuración de los botónes con íconos
del portafolio.
"""

import reflex as rx


def icon_button(icon: str, url: str, text="", solid=False) -> rx.Component:
    """
    Método que regresa un botón con un ícono dada
    una configuración previa.

    Args
    ----
        icon (str): Nombre del ícono a usar.
        url (str): URL a incluir en el botón al ser accionado.
        text (str, optional): Texto a incluir en el botón. "" por default.
        solid (bool, optional): Variante a usar del botón. "Solid" por default.

    Returns:
        rx.Component: _description_
    """
    return rx.link(
        rx.button(rx.icon(icon), text, variant="solid" if solid else "surface"),
        href=url,
        is_external=True,
    )
