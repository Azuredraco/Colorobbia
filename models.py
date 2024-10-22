from extensions import db


class Cuestionario(db.Model):
    """Model representing a questionnaire."""

    id = db.Column(
        db.String(8), primary_key=True
    )  # Unique identifier for the questionnaire
    manager_id = db.Column(
        db.String(8), nullable=False
    )  # ID of the manager associated with the questionnaire
    tipo = db.Column(
        db.Boolean, nullable=False
    )  # Indicates if the questionnaire is for a manager (True) or team (False)
    frase_semilla = db.Column(
        db.String(100), unique=True, nullable=False
    )  # Unique seed phrase for the questionnaire
    usado = db.Column(
        db.Boolean, default=False
    )  # Indicates if the questionnaire has been used

    def __repr__(self):
        """Return a string representation of the Cuestionario instance."""
        return f"<Cuestionario {self.id!r}>"


class Respuesta(db.Model):
    """Model representing a response to a questionnaire."""

    cuestionario_id = db.Column(
        db.String(8), db.ForeignKey("cuestionario.id"), nullable=False
    )  # Foreign key referencing the associated questionnaire
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for the response
    id_pregunta = db.Column(
        db.Integer, nullable=False
    )  # ID of the question being answered
    respuesta = db.Column(db.Integer, nullable=False)  # The response value
    timestamp = db.Column(
        db.DateTime, nullable=False
    )  # Timestamp of when the response was recorded

    def __repr__(self):
        """Return a string representation of the Respuesta instance."""
        return f"<Respuesta {self.id!r}>"
