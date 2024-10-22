import json
import os

from flask import Flask

from extensions import db
from models import Cuestionario
from routes import main


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///colorobbia.db"
    app.config["SECRET_KEY"] = os.urandom(24)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()
        if Cuestionario.query.count() == 0:
            with open("questionnaires.json", "r", encoding="utf-8") as f:
                cuestionarios = json.load(f)
            # Collect all Cuestionario objects in a list
            cuestionario_objects = [
                Cuestionario(
                    id=c["id"],
                    tipo=c["type"],
                    manager_id=c["manager_id"],
                    frase_semilla=c["seed_phrase"],
                )
                for c in cuestionarios
            ]
            # Perform a bulk insert
            db.session.bulk_save_objects(cuestionario_objects)
            db.session.commit()
        print(
            f"Número de cuestionarios en la base de datos: {Cuestionario.query.count()}"
        )

    app.register_blueprint(main)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
