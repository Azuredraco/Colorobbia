import random

# Hard-coded data after processing the CSV content
PREGUNTAS = {
    1: (
        "¿Se comunica de manera clara y efectiva?",
        "¿Me comunico de manera clara y efectiva?",
    ),
    2: (
        "¿Escucha activamente y valora las opiniones de los demás?",
        "¿Escucho activamente y valoro las opiniones de los demás?",
    ),
    3: (
        "¿Proporciona información de tu desempeño de manera constructiva y orientada a la mejora?",
        "¿Proporciono información sobre el desempeño de manera constructiva y orientada a la mejora?",
    ),
    4: (
        "¿Es claro/a en sus instrucciones y objetivos?",
        "¿Soy claro/a en mis instrucciones y objetivos?",
    ),
    5: (
        "¿Muestra empatía y comprensión al responder a las preocupaciones y necesidades de los demás?",
        "¿Muestro empatía y comprensión al responder a las preocupaciones y necesidades de los demás?",
    ),
    6: (
        "¿Fomenta un ambiente de trabajo de confianza y colaboración?",
        "¿Fomento un ambiente de trabajo de confianza y colaboración?",
    ),
    7: (
        "¿Promueve la diversidad de ideas y permite que se participe en la búsqueda de soluciones?",
        "¿Promuevo la diversidad de ideas y permito que se participe en la búsqueda de soluciones?",
    ),
    8: (
        "¿Te ofrece sugerencias y oportunidades de mejora?",
        "¿Ofrezco sugerencias y oportunidades de mejora a mi equipo?",
    ),
    9: (
        "¿Toma decisiones informadas y considera diferentes opiniones y perspectivas de todas las personas?",
        "¿Tomo decisiones informadas y considero diferentes opiniones y perspectivas de todas las personas?",
    ),
    10: (
        "¿Es capaz de tomar decisiones rápidas y efectivas en situaciones de presión?",
        "¿Soy capaz de tomar decisiones rápidas y efectivas en situaciones de presión?",
    ),
    11: (
        "¿Asume la responsabilidad de sus decisiones y, si sucede, acepta que cometió un error?",
        "¿Asumo la responsabilidad de mis decisiones y, si sucede, acepto que cometí un error?",
    ),
    12: (
        "¿Genera un entorno de confianza y la gente se atreve a comentar los errores, propios y ajenos?",
        "¿Genero un entorno de confianza donde la gente se atreve a comentar los errores, propios y ajenos?",
    ),
    13: (
        "¿Ayuda a su equipo a priorizar tareas y manejar la carga de trabajo de manera efectiva?",
        "¿Ayudo a mi equipo a priorizar tareas y manejar la carga de trabajo de manera efectiva?",
    ),
    14: (
        "¿Asigna tareas y responsabilidades de manera equitativa y realista?",
        "¿Asigno tareas y responsabilidades de manera equitativa y realista?",
    ),
    15: (
        "¿Establece objetivos claros y realistas?",
        "¿Establezco objetivos claros y realistas?",
    ),
    16: (
        "¿Si tienes dudas le puedes preguntar y te ayuda a resolverlas?",
        "¿Si mi equipo tiene dudas, estoy disponible para ayudar a resolverlas?",
    ),
    17: (
        "¿Promueve un ambiente de trabajo positivo y reconoce los logros ajenos?",
        "¿Promuevo un ambiente de trabajo positivo y reconozco los logros de los demás?",
    ),
    18: (
        "¿Ejerce una supervisión adecuada a tus necesidades?",
        "¿Ejerzo una supervisión adecuada a las necesidades de mi equipo?",
    ),
    19: (
        "¿Tiene capacidad y asertividad para gestionar conflictos?",
        "¿Tengo capacidad y asertividad para gestionar conflictos?",
    ),
    20: (
        "Cuando se producen situaciones de tensión entre o con las personas de su equipo, ¿gestiona la situación de manera justa y equitativa?",
        "Cuando se producen situaciones de tensión entre o con las personas de mi equipo, ¿gestiono la situación de manera justa y equitativa?",
    ),
    21: (
        "¿Busca constantemente oportunidades de aprendizaje y desarrollo personal propio y para el equipo?",
        "¿Busco constantemente oportunidades de aprendizaje y desarrollo personal propio y para el equipo?",
    ),
    22: (
        "¿Gestiona los imprevistos de manera eficiente sin comprometer la calidad del trabajo y el ambiente del equipo?",
        "¿Gestiono los imprevistos de manera eficiente sin comprometer la calidad del trabajo y el ambiente del equipo?",
    ),
    23: (
        "¿Consideras que gestiona bien sus emociones cuando se producen momentos de tensión?",
        "¿Considero que gestiono bien mis emociones cuando se producen momentos de tensión?",
    ),
    24: (
        "¿Respeta el horario no laboral y permite la desconexión digital?",
        "¿Respeto el horario no laboral y permito la desconexión digital?",
    ),
    25: (
        "¿Actúa de manera inmediata cuando observa alguna situación discriminatoria en el equipo?",
        "¿Actúo de manera inmediata cuando observo alguna situación discriminatoria en el equipo?",
    ),
}

# Create a mapping of tematica to question IDs
TEMATICA = {
    "Comunicación Efectiva": [1, 2, 4],
    "Feedback y reconocimiento": [3, 8, 17],
    "Inteligencia Emocional": [5, 18, 23],
    "Participación y Trabajo en Equipo": [6, 7, 9],
    "Liderazgo Efectivo": [10, 13, 14, 15, 22, 24],
    "Confianza y aprendizaje": [11, 12, 16, 21],
    "Gestión de Conflictos": [19, 20, 25],
}

# Define the palabras list
PALABRAS = [
    "azulejo",
    "barniz",
    "bicocción",
    "brillo",
    "cerámica",
    "colorante",
    "decoración",
    "engobe",
    "esmalte",
    "frita",
    "granilla",
    "gres",
    "horno",
    "micronizado",
    "monoporosa",
    "opacidad",
    "pigmento",
    "porcelana",
    "tinta",
    "vidrio",
]


def generate_seed_phrase():
    return " ".join(random.choices(PALABRAS, k=5))


def obtener_preguntas(tipo):
    # tipo should be a boolean: True for "mando", False for "equipo"
    return [pregunta[1] if tipo else pregunta[0] for pregunta in PREGUNTAS.values()]
