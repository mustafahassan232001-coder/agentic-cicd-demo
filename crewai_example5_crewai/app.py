from flask import Flask
from flask_login import LoginManager
from database import db, init_db
from models import User
from auth import auth_bp
from tasks import tasks_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = 'dev-key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

init_db(app)
app.register_blueprint(auth_bp)
app.register_blueprint(tasks_bp)

if __name__ == '__main__':
    app.run(debug=True)