"""

Control unificador de los proyectos secundarios a incluir
en el portafolio.
"""

import reflex as rx
from portafolio.components.card_detail import card_detail
from portafolio.components.heading import heading
from portafolio.data import Extra
from portafolio.styles.styles import Size


def extra(extras: list[Extra]) -> rx.Component:
    """
    Método que, dada una lista de tipo Extra (los proyectos
    secundarios), crea un vstack con vistas de tarjeta de c/u
    de los elementos ingresados.

    Args
    ----
        extras (list[Extra]): Lista de proyectos secundarios a integrar al portafolio.

    Returns
    -------
        rx.Component: Regresa un vstack con las vistas de tarjeta de los proyectos secundarios.
    """
    return rx.vstack(
        heading("Secondary Projects "),
        rx.mobile_only(
            rx.vstack(*[card_detail(extra) for extra in extras], spacing=Size.DEFAULT.value),
            width="100%",
        ),
        rx.tablet_and_desktop(
            rx.grid(
                *[card_detail(extra) for extra in extras],
                spacing=Size.DEFAULT.value,
                columns="3",
            ),
            width="100%",
        ),
        spacing=Size.DEFAULT.value,
        width="100%",
    )
