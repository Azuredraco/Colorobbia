import json
import os

from flask import Flask

from extensions import db
from models import Cuestionario
from routes import main


def create_app():
    """Create and configure a Flask application."""

    # Initialize the Flask application
    app = Flask(__name__)

    # Configure the database URI and other settings
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///colorobbia.db"
    app.config["SECRET_KEY"] = os.urandom(24)  # Generate a random secret key
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = (
        False  # Disable modification tracking
    )

    # Initialize the database with the app context
    db.init_app(app)

    with app.app_context():
        # Create the database tables
        db.create_all()

        # Check if there are any existing questionnaires
        if Cuestionario.query.count() == 0:
            # Load questionnaires from a JSON file
            with open("questionnaires.json", "r", encoding="utf-8") as f:
                cuestionarios = json.load(f)

            # Bulk insert the loaded questionnaires into the database
            db.session.bulk_save_objects(
                Cuestionario(
                    id=c["id"],
                    manager_id=c["manager_id"],
                    tipo=c["id"] == c["manager_id"],  # Determine type based on IDs
                    frase_semilla=c["seed_phrase"],
                )
                for c in cuestionarios
            )
            db.session.commit()  # Commit the transaction

        # Print the number of questionnaires in the database
        print(
            f"Número de cuestionarios en la base de datos: {Cuestionario.query.count()}"
        )

    # Register the main blueprint for the application
    app.register_blueprint(main)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
