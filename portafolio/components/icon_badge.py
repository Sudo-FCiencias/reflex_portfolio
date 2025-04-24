"""
Configuración de las badges del portafolio.
"""

import reflex as rx


def icon_badge(icon: str) -> rx.Component:
    """
    Genera una badge con un ícono.

    Args
    ----
        icon (str): Nombre del ícono a usar.

    Returns:
        rx.Component: Badge con el ićono.
    """
    return rx.badge(rx.icon(icon, size=32), aspect_ratio="1", variant="soft")
