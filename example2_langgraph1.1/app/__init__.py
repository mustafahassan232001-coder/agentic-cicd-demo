from flask import Flask
from .database import init_db

def create_app():
    app = Flask(__name__)
    app.config['DATABASE'] = 'tasks.db'
    
    # Initialize with the configured database path
    init_db(app.config['DATABASE'])
    
    from .routes import task_bp
    app.register_blueprint(task_bp)
    
    return app
