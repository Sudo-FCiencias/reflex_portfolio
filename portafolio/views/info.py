"""
Unificador de los vstacks usados para incluir proyectos,
experiencia laboral y estudios en el portafolio.

"""

import reflex as rx

from portafolio.components.heading import heading
from portafolio.components.info_detail import info_detail
from portafolio.data import Info
from portafolio.styles.styles import Size


def info(title: str, information: list[Info]) -> rx.Component:
    """
    Método que unifica la generación de la serie de
    componentes necesarios para incluir las secciones
    de experiencia laboral, estudios y proyectos.

    Args
    ----
        title (str): Título a usar para la sección de información.
        info (list[Info]): Lista de tipo Info con los datos de cada estudio, projecto, etc.

    Returns
    -------
        rx.Component: VStack con los componentes generados para los elementos de info.
    """
    return rx.vstack(
        heading(title),
        rx.vstack(
            *[info_detail(item) for item in information],
            spacing=Size.DEFAULT.value,
            width="100%",
        ),
        spacing=Size.DEFAULT.value,
        width="100%",
    )
