from flask import Flask
from routes import tasks_bp
from errors import errors_bp


app = Flask(__name__)

# חיבור כל ה-blueprints
app.register_blueprint(tasks_bp)
app.register_blueprint(errors_bp)



if __name__ == "__main__":
    app.run(debug=True)