"""
Archivo con las clases de las distintas secciónes del portafolio.
"""

import json


class Media:
    """
    Clase para representar la multimedia del usuario del portafolio.

    Atributos
    ---------
    email: str
        Correo Electrónico a referenciar en el portafolio.
    cv: file
        Archivo a usar para un botón específico en la WebApp.
    github: str
        Enlace de GitHub del usuario.
    linkedln: str
        Enlace de Linkedin del usurio.
    """

    def __init__(self, email, cv, github, linkedin):
        self.email = email
        self.cv = cv
        self.github = github
        self.linkedin = linkedin


class Technology:
    """
    Clase para representar las tecnologías usadas por el usuario

    Atributos
    --------
    icon: str
        Ícono de la tecnología. Se referencia de DevIcons.
    name: str
        Nombre de la técnología en cuestión.
    """

    def __init__(self, icon, name):
        self.icon = icon
        self.name = name


class Language:
    """
    Clase para representar los lenguajes (no de programación)
    usados por el usuario.

    Atributos
    ---------
    icon: str
        Ícono del lenguaje. Se referencia de DevIcons (de existir)
    name: str
        Nombre del lenguaje en cuestión.
    """

    def __init__(self, icon, name):
        self.icon = icon
        self.name = name


class Info:
    """
    La clase representa un conjunto de información en particular sobre un tema del portafolio.
    Por ejemplo, puede ser usada para incluir información de proyectos, pero también puede usarse
    para incluir formación académica y/o experiencia laboral.

    Para un mejor entendimiento se recomienda revisar assets/data/data.json

    Atributos
    ---------
    icon: str
        Ícono de la información en cuestión. Se referencia de DevIcons.
    title: str
        Nombre de la información. ie: Nombre de una Certificación.
    subtitle: str
        Subtítulo de información. ie: Ligera explicación de la certificación.
    description: str
        Descripción de la información. ie: Conocimiento validado por una certificación.
    date: str
        Fecha de la información. ie: 2024-2025.
    certificate: str
        URL de la información. Más pensado hacia certificaciones.
    technologies: [str]
        Lista de technologías usadas de la información ingresada. ie: Lenguajes/Frameworks.
    image: str
        Dirección de la imágen a usar para representar el bloque de información.
    url: str
        URL del bloque de información específico (de existir).
    github: str
        URL del repositorio de GitHub del bloque de información en cuestión.
    """

    def __init__(
        self,
        icon,
        title,
        subtitle,
        description,
        date="",
        certificate="",
        technologies=[],
        image="",
        url="",
        github="",
    ):
        self.icon = icon
        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.date = date
        self.certificate = certificate
        self.technologies = [Technology(**tech) for tech in technologies]
        self.image = image
        self.url = url
        self.github = github


class Extra:
    """
    Clase usada para representar información de proyectos secundarios.
    Por ejemplo, participaciónes en una comunidad, etc.

    Atributos
    ---------
    image: str
        Dirección de la imágen a usar para representar el bloque de información.
    title: str
        Nombre de la información. ie: Nombre de una comunidad.
    description: str
        Descripción de la información. ie: Charla dada en una comunidad.
    url: str
        URL del bloque del proyecto secundario específico.
    """

    def __init__(self, image, title, description, url):
        self.image = image
        self.title = title
        self.description = description
        self.url = url


class Data:
    """
    Data es la clase unificadora de las distintas secciones del portafolio.
    Añadido a las secciones, Data incluye atributos más personales sobre quien
    esté haciendo el portafolio.

    Atributos
    ---------
    title: str
        Titulo del portafolio. Esto está más pensado hacia el título de la página del portafolio,
        como un atributo HTML.
    description: str
        Descripción del portafolio. Esto está más pensado hacia la descripción de la página del
        portafolio, como un atributo HTML.
    image/avatar: str
        Imágen a usar de avatar para el portafio.
    name: str
        Nombre del usuario del portafolio.
    skill: str
        Aptitudes a destacar. ie: Ingeniero de Software.
    location: str
        Ubicación del usuario del portafolio.
    media: [str]
        Lista de URLs usadas para los atributos de la clase Media
    about: str
        Texto a usar como descripción del usuario. No más de 4 líneas.
    technologies: [str]
        Lista de tecnologias usadas para los atributos de la clase Technology
    languages: [str]
        Lista de lenguajes (no de programación) usados para los atributos de la clase Language.
    experience:
        Experiencia Laboral del usuario a usar usando Info.
    projects:
        Proyectos del usuario a usar usando Info.
    training:
        Experiencia Académica del usuario a usar usando Info.
    extras:
        Proyectos secundarios del usuario a usar usando Info.

    """

    def __init__(
        self,
        title,
        description,
        image,
        avatar,
        name,
        skill,
        location,
        media,
        about,
        technologies,
        languages,
        experience,
        projects,
        training,
        extras,
    ):
        self.title = title
        self.description = description
        self.image = image
        self.avatar = avatar
        self.name = name
        self.skill = skill
        self.location = location
        self.media = Media(**media)
        self.about = about
        self.technologies = [Technology(**tech) for tech in technologies]
        self.languages = [Language(**lang) for lang in languages]
        self.experience = [Info(**info) for info in experience]
        self.projects = [Info(**info) for info in projects]
        self.training = [Info(**info) for info in training]
        self.extras = [Extra(**info) for info in extras]


# Recuerda cambiar al archivo que necesitas.
with open("assets/data/data.json", mode="r", encoding="utf-8") as file:
    json_data = json.load(file)

data = Data(**json_data)
