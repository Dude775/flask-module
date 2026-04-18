from flask import Flask
from routes import todos_bp
from errors import errors_bp

app = Flask(__name__)

# חיבור כל ה-blueprints
app.register_blueprint(todos_bp)
app.register_blueprint(errors_bp)

if __name__ == "__main__":
    app.run(debug=True)
