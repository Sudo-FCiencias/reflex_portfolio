"""
"Galeria" de tamaños y de hojas de estilo a usar a lo
largo del portafolio.
"""

from enum import Enum
import reflex as rx

MAX_WIDTH = "900px"
IMAGE_HEIGHT = "200px"


class EmSize(Enum):
    """
    Clase para representar los tamaños
    EM dado un Enum.

    Args
    ----
        Enum : Enum usado para los distintos valores EM.
    """

    DEFAULT = "1em"  # 16px
    MEDIUM = "2em"
    BIG = "4em"


class Size(Enum):
    """
    Clase para representar los tamaños
    en generales (en pixeles) dado un Enum.

    Args
    ----
        Enum : Enum usado para los distintos valores px.
    """

    ZERO = "0"
    SMALL = "2"  # 8px
    DEFAULT = "4"  # 16px/1em
    MEDIUM = "6"  # 32px
    BIG = "8"  # 48px


STYLESHEETS = [
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css",
    # "/fonts/fonts.css"
]

BASE_STYLE = {rx.button: {"--cursor-button": "pointer"}}
