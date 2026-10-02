from flask import Flask
from database import init_db
from routes import tasks_bp

app = Flask(__name__)
app.register_blueprint(tasks_bp)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
