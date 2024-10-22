# Hard-coded data after processing the CSV content
import random

PREGUNTAS = [
    {
        "id": 1,
        "equipo": "¿Se comunica de manera clara y efectiva?",
        "mando": "¿Me comunico de manera clara y efectiva?",
        "tematica": "Comunicación Efectiva",
    },
    {
        "id": 2,
        "equipo": "¿Escucha activamente y valora las opiniones de los demás?",
        "mando": "¿Escucho activamente y valoro las opiniones de los demás?",
        "tematica": "Comunicación Efectiva",
    },
    {
        "id": 3,
        "equipo": "¿Proporciona información de tu desempeño de manera constructiva y orientada a la mejora?",
        "mando": "¿Proporciono información sobre el desempeño de manera constructiva y orientada a la mejora?",
        "tematica": "Feedback y reconocimiento",
    },
    {
        "id": 4,
        "equipo": "¿Es claro/a en sus instrucciones y objetivos?",
        "mando": "¿Soy claro/a en mis instrucciones y objetivos?",
        "tematica": "Comunicación Efectiva",
    },
    {
        "id": 5,
        "equipo": "¿Muestra empatía y comprensión al responder a las preocupaciones y necesidades de los demás?",
        "mando": "¿Muestro empatía y comprensión al responder a las preocupaciones y necesidades de los demás?",
        "tematica": "Inteligencia Emocional",
    },
    {
        "id": 6,
        "equipo": "¿Fomenta un ambiente de trabajo de confianza y colaboración?",
        "mando": "¿Fomento un ambiente de trabajo de confianza y colaboración?",
        "tematica": "Participación y Trabajo en Equipo",
    },
    {
        "id": 7,
        "equipo": "¿Promueve la diversidad de ideas y permite que se participe en la búsqueda de soluciones?",
        "mando": "¿Promuevo la diversidad de ideas y permito que se participe en la búsqueda de soluciones?",
        "tematica": "Participación y Trabajo en Equipo",
    },
    {
        "id": 8,
        "equipo": "¿Te ofrece sugerencias y oportunidades de mejora?",
        "mando": "¿Ofrezco sugerencias y oportunidades de mejora a mi equipo?",
        "tematica": "Feedback y reconocimiento",
    },
    {
        "id": 9,
        "equipo": "¿Toma decisiones informadas y considera diferentes opiniones y perspectivas de todas las personas?",
        "mando": "¿Tomo decisiones informadas y considero diferentes opiniones y perspectivas de todas las personas?",
        "tematica": "Participación y Trabajo en Equipo",
    },
    {
        "id": 10,
        "equipo": "¿Es capaz de tomar decisiones rápidas y efectivas en situaciones de presión?",
        "mando": "¿Soy capaz de tomar decisiones rápidas y efectivas en situaciones de presión?",
        "tematica": "Liderazgo Efectivo",
    },
    {
        "id": 11,
        "equipo": "¿Asume la responsabilidad de sus decisiones y, si sucede, acepta que cometió un error?",
        "mando": "¿Asumo la responsabilidad de mis decisiones y, si sucede, acepto que cometí un error?",
        "tematica": "Confianza y aprendizaje",
    },
    {
        "id": 12,
        "equipo": "¿Genera un entorno de confianza y la gente se atreve a comentar los errores, propios y ajenos?",
        "mando": "¿Genero un entorno de confianza donde la gente se atreve a comentar los errores, propios y ajenos?",
        "tematica": "Confianza y aprendizaje",
    },
    {
        "id": 13,
        "equipo": "¿Ayuda a su equipo a priorizar tareas y manejar la carga de trabajo de manera efectiva?",
        "mando": "¿Ayudo a mi equipo a priorizar tareas y manejar la carga de trabajo de manera efectiva?",
        "tematica": "Liderazgo Efectivo",
    },
    {
        "id": 14,
        "equipo": "¿Asigna tareas y responsabilidades de manera equitativa y realista?",
        "mando": "¿Asigno tareas y responsabilidades de manera equitativa y realista?",
        "tematica": "Liderazgo Efectivo",
    },
    {
        "id": 15,
        "equipo": "¿Establece objetivos claros y realistas?",
        "mando": "¿Establezco objetivos claros y realistas?",
        "tematica": "Liderazgo Efectivo",
    },
    {
        "id": 16,
        "equipo": "¿Si tienes dudas le puedes preguntar y te ayuda a resolverlas?",
        "mando": "¿Si mi equipo tiene dudas, estoy disponible para ayudar a resolverlas?",
        "tematica": "Confianza y aprendizaje",
    },
    {
        "id": 17,
        "equipo": "¿Promueve un ambiente de trabajo positivo y reconoce los logros ajenos?",
        "mando": "¿Promuevo un ambiente de trabajo positivo y reconozco los logros de los demás?",
        "tematica": "Feedback y reconocimiento",
    },
    {
        "id": 18,
        "equipo": "¿Ejerce una supervisión adecuada a tus necesidades?",
        "mando": "¿Ejerzo una supervisión adecuada a las necesidades de mi equipo?",
        "tematica": "Inteligencia Emocional",
    },
    {
        "id": 19,
        "equipo": "¿Tiene capacidad y asertividad para gestionar conflictos?",
        "mando": "¿Tengo capacidad y asertividad para gestionar conflictos?",
        "tematica": "Gestión de Conflictos",
    },
    {
        "id": 20,
        "equipo": "Cuando se producen situaciones de tensión entre o con las personas de su equipo, ¿gestiona la situación de manera justa y equitativa?",
        "mando": "Cuando se producen situaciones de tensión entre o con las personas de mi equipo, ¿gestiono la situación de manera justa y equitativa?",
        "tematica": "Gestión de Conflictos",
    },
    {
        "id": 21,
        "equipo": "¿Busca constantemente oportunidades de aprendizaje y desarrollo personal propio y para el equipo?",
        "mando": "¿Busco constantemente oportunidades de aprendizaje y desarrollo personal propio y para el equipo?",
        "tematica": "Confianza y aprendizaje",
    },
    {
        "id": 22,
        "equipo": "¿Gestiona los imprevistos de manera eficiente sin comprometer la calidad del trabajo y el ambiente del equipo?",
        "mando": "¿Gestiono los imprevistos de manera eficiente sin comprometer la calidad del trabajo y el ambiente del equipo?",
        "tematica": "Liderazgo Efectivo",
    },
    {
        "id": 23,
        "equipo": "¿Consideras que gestiona bien sus emociones cuando se producen momentos de tensión?",
        "mando": "¿Considero que gestiono bien mis emociones cuando se producen momentos de tensión?",
        "tematica": "Inteligencia Emocional",
    },
    {
        "id": 24,
        "equipo": "¿Respeta el horario no laboral y permite la desconexión digital?",
        "mando": "¿Respeto el horario no laboral y permito la desconexión digital?",
        "tematica": "Liderazgo Efectivo",
    },
    {
        "id": 25,
        "equipo": "¿Actúa de manera inmediata cuando observa alguna situación discriminatoria en el equipo?",
        "mando": "¿Actúo de manera inmediata cuando observo alguna situación discriminatoria en el equipo?",
        "tematica": "Gestión de Conflictos",
    },
]

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
    return [pregunta[tipo] for pregunta in PREGUNTAS]


# Uncomment if needed
"""
def obtener_tematicas():
    return list({pregunta['tematica'] for pregunta in preguntas})

def obtener_preguntas_por_tematica(tipo):
    tematica_dict = {}
    for pregunta in preguntas:
        tematica = pregunta['tematica']
        if tematica not in tematica_dict:
            tematica_dict[tematica] = []
        tematica_dict[tematica].append(pregunta[tipo])
    return tematica_dict
"""
