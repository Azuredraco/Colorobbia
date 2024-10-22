from datetime import datetime

from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from extensions import db
from models import Cuestionario, Respuesta
from utils import PALABRAS, obtener_preguntas

# Create a blueprint for the main application routes
main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def index():
    """Render the index page and handle seed phrase submission."""
    if request.method == "POST":
        # Construct the seed phrase from form inputs
        frase_semilla = " ".join(request.form[f"palabra{i}"] for i in range(1, 6))

        # Check if the seed phrase corresponds to an existing questionnaire
        if cuestionario := Cuestionario.query.filter_by(
            frase_semilla=frase_semilla
        ).first():
            if cuestionario.usado:
                return redirect(
                    url_for("main.ya_respondido")
                )  # Redirect if already answered

            session["cuestionario_id"] = (
                cuestionario.id
            )  # Store questionnaire ID in session
            return redirect(
                url_for("main.cuestionario")
            )  # Redirect to the questionnaire page
        else:
            flash(
                "Frase semilla inválida. Por favor, intente de nuevo."
            )  # Flash error message

    return render_template("index.html", palabras=PALABRAS)  # Render the index template


@main.route("/cuestionario", methods=["GET", "POST"])
def cuestionario():
    """Render the questionnaire page and handle responses."""
    if "cuestionario_id" not in session:
        return redirect(
            url_for("main.index")
        )  # Redirect if no questionnaire ID in session

    cuestionario = Cuestionario.query.get(
        session["cuestionario_id"]
    )  # Retrieve the questionnaire

    if request.method == "POST":
        # Collect responses from the form
        respuestas = [
            Respuesta(
                cuestionario_id=cuestionario.id,
                id_pregunta=int(id_pregunta.split("_")[1]),  # Extract question ID
                respuesta=int(respuesta),  # Convert response to integer
                timestamp=datetime.now(),  # Record the current timestamp
            )
            for id_pregunta, respuesta in request.form.items()
            if id_pregunta.startswith("pregunta_")  # Filter for question responses
        ]
        db.session.add_all(respuestas)  # Add all responses to the session

        cuestionario.usado = True  # Mark the questionnaire as used
        db.session.commit()  # Commit the transaction

        return redirect(
            url_for("main.agradecimiento")
        )  # Redirect to the thank you page

    preguntas = obtener_preguntas(
        cuestionario.tipo
    )  # Retrieve questions based on questionnaire type
    return render_template(
        "cuestionario.html", preguntas=preguntas
    )  # Render the questionnaire template


@main.route("/agradecimiento")
def agradecimiento():
    """Render the thank you page after questionnaire completion."""
    return render_template("agradecimiento.html")  # Render the thank you template


@main.route("/ya_respondido")
def ya_respondido():
    """Render the page indicating the questionnaire has already been answered."""
    return render_template("ya_respondido.html")  # Render the already answered template


@main.route("/database")
def database_content():
    """Render the database content page showing all questionnaires and responses."""
    cuestionarios = Cuestionario.query.all()  # Retrieve all questionnaires
    respuestas = Respuesta.query.all()  # Retrieve all responses
    return render_template(
        "database.html", cuestionarios=cuestionarios, respuestas=respuestas
    )  # Render the database content template
