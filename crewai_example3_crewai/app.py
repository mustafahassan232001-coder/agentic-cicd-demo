from flask import Flask
from database import init_db
from routes import expense_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    init_db(app)
    app.register_blueprint(expense_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)