"""
Vista de la sección "Sobre Mi" del portafolio.
"""

import reflex as rx
from portafolio.components.heading import heading


def about(description: str) -> rx.Component:
    """_summary_

    Args
    ----
        description (str): Información a incluir en la sección.

    Returns
    -------
        rx.Component: Componente de Reflex con la información de la sección.
    """

    return rx.vstack(heading("About Me "), rx.text(description))
