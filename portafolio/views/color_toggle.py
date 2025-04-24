"""
Switcher de tema para el portafolio.

"""

import reflex as rx
from reflex.style import set_color_mode, color_mode


def color_toggle() -> rx.Component:
    """
    Método que cambia el tema de color del portafolio usando
    dos botones.

    Returns
    -------
        rx.Component: Controles de cambio de tema de color.
    """
    return rx.segmented_control.root(
        rx.segmented_control.item(
            rx.icon(tag="sun", size=20),
            value="light",
        ),
        rx.segmented_control.item(
            rx.icon(tag="moon", size=20),
            value="dark",
        ),
        on_change=set_color_mode,
        variant="classic",
        radius="full",
        value=color_mode,
    )
