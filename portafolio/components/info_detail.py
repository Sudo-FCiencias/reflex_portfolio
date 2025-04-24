"""

Generador del HStack usado para los diferentes tipos de información
a incluir en el portafolio.

Notese que según lo que se incluya en cada sección de data.json
será la información a reenderizar por este componente.

"""

import reflex as rx
from portafolio.components.icon_badge import icon_badge
from portafolio.components.icon_button import icon_button
from portafolio.data import Info
from portafolio.styles.styles import IMAGE_HEIGHT, EmSize, Size


def info_detail(info: Info) -> rx.Component:
    """
    Método para generár el HStack necesario para las
    secciones de proyectos, educación y experiencia
    laboral del portafolio.

    Args
    ----
        info (Info): Ejemplar de la clase Info para obtener la información a incluir.

    Returns:
        rx.Component: HStack con la información prevista en info.
    """
    return rx.flex(
        rx.hstack(
            icon_badge(info.icon),
            rx.vstack(
                rx.text.strong(info.title),
                rx.text(info.subtitle),
                rx.text(info.description, size=Size.SMALL.value, color_scheme="gray"),
                # * Se supone que aqui va la lista de tecnologias usadas en c/proyecto pero
                # * es más facil escribirlas en texto plano. La razón de que esto no se pueda
                # * incluir de momento es un problema de las versiones de reflex >=0.6
                rx.hstack(rx.cond(info.github != "", icon_button("github", info.github))),
                spacing=Size.SMALL.value,
                width="100%",
            ),
            spacing=Size.DEFAULT.value,
            width="100%",
        ),
        rx.cond(
            info.image != "",
            rx.image(
                src=info.image,
                height=IMAGE_HEIGHT,
                width="auto",
                border_radius=EmSize.DEFAULT.value,
                object_fit="cover",
            ),
        ),
        rx.vstack(
            rx.cond(info.date != "", rx.badge(info.date, size="2")),
            rx.cond(
                info.certificate != "",
                icon_button("shield-check", info.certificate, solid=True),
            ),
            spacing=Size.SMALL.value,
            align="end",
        ),
        flex_direction=["column-reverse", "row"],
        spacing=Size.DEFAULT.value,
        width="100%",
    )
