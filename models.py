from extensions import db


class Cuestionario(db.Model):
    id = db.Column(db.String(8), primary_key=True)  # Moved to the top
    manager_id = db.Column(db.String(8), nullable=False)  # manager_id follows id
    tipo = db.Column(db.Boolean, nullable=False)  # Changed to Boolean
    frase_semilla = db.Column(db.String(100), unique=True, nullable=False)
    usado = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Cuestionario {self.id!r}>"


class Respuesta(db.Model):
    cuestionario_id = db.Column(
        db.String(8), db.ForeignKey("cuestionario.id"), nullable=False
    )
    id = db.Column(db.Integer, primary_key=True)  # ID follows cuestionario_id
    id_pregunta = db.Column(db.Integer, nullable=False)
    respuesta = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Respuesta {self.id!r}>"
