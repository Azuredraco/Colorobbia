from extensions import db


class Cuestionario(db.Model):
    id = db.Column(db.String(8), primary_key=True)
    tipo = db.Column(db.String(10), nullable=False)
    manager_id = db.Column(db.String(8), nullable=False)
    frase_semilla = db.Column(db.String(100), unique=True, nullable=False)
    usado = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Cuestionario {self.id!r}>"


class Respuesta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cuestionario_id = db.Column(
        db.String(8), db.ForeignKey("cuestionario.id"), nullable=False
    )
    id_pregunta = db.Column(db.Integer, nullable=False)
    respuesta = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Respuesta {self.id!r}>"
