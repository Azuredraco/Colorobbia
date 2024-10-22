from datetime import datetime

from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from extensions import db
from models import Cuestionario, Respuesta
from utils import PALABRAS, obtener_preguntas

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        frase_semilla = " ".join(request.form[f"palabra{i}"] for i in range(1, 6))
        if cuestionario := Cuestionario.query.filter_by(
            frase_semilla=frase_semilla
        ).first():
            if cuestionario.usado:
                return redirect(url_for("main.ya_respondido"))
            session["cuestionario_id"] = cuestionario.id
            return redirect(url_for("main.cuestionario"))
        else:
            flash("Frase semilla inválida. Por favor, intente de nuevo.")

    return render_template("index.html", palabras=PALABRAS)


@main.route("/cuestionario", methods=["GET", "POST"])
def cuestionario():
    if "cuestionario_id" not in session:
        return redirect(url_for("main.index"))

    cuestionario = Cuestionario.query.get(session["cuestionario_id"])

    if request.method == "POST":
        respuestas = [
            Respuesta(
                cuestionario_id=cuestionario.id,
                id_pregunta=int(id_pregunta.split("_")[1]),
                respuesta=int(respuesta),
                timestamp=datetime.now(),
            )
            for id_pregunta, respuesta in request.form.items()
            if id_pregunta.startswith("pregunta_")
        ]
        db.session.add_all(respuestas)

        cuestionario.usado = True
        db.session.commit()

        return redirect(url_for("main.agradecimiento"))

    preguntas = obtener_preguntas(cuestionario.tipo)
    return render_template("cuestionario.html", preguntas=preguntas)


@main.route("/agradecimiento")
def agradecimiento():
    return render_template("agradecimiento.html")


@main.route("/ya_respondido")
def ya_respondido():
    return render_template("ya_respondido.html")


@main.route("/database")
def database_content():
    cuestionarios = Cuestionario.query.all()
    respuestas = Respuesta.query.all()
    return render_template(
        "database.html", cuestionarios=cuestionarios, respuestas=respuestas
    )
