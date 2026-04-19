from flask import Flask, render_template
from db import init_db
from routes import todos_bp
from errors import errors_bp

app = Flask(__name__)

init_db(app)

# חיבור כל ה-blueprints
app.register_blueprint(todos_bp)
app.register_blueprint(errors_bp)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
