"""

Componentente para generar las tarjetas de información extra
del portafolio. Está pensada más hacia proyectos secundarios,
pues importa de la clase Extra.

"""

import reflex as rx
from portafolio.data import Extra

from portafolio.styles.styles import IMAGE_HEIGHT, Size


def card_detail(extra: Extra) -> rx.Component:
    """
    Método para generar una tarjeta de información de un
    proyecto dada una imágen y su descripción.

    Args
    ----
        extra (Extra): Información sobre la que se hará la tarjeta.

    Returns
    -------
        rx.Component: Tarjeta con la información del proyecto.
    """
    return rx.card(
        rx.link(
            rx.inset(
                rx.image(
                    src=extra.image,
                    height=IMAGE_HEIGHT,
                    width="550%",
                    object_fit="cover",
                ),
                pb="current",
                side="top",
            ),
            rx.text.strong(extra.title),
            rx.text(extra.description, size=Size.SMALL.value, color_scheme="gray"),
        ),
        width="90%",
        href=extra.url,
        is_external=True,
    )
