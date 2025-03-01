import os
from flask import Flask
from app.api.vision_api import vision_api

def create_app():
    app = Flask(__name__)
    
    # Configure app
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload size
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key-for-testing')
    
    # Create upload folder if it doesn't exist
    upload_folder = os.path.join(app.static_folder, 'uploads')
    os.makedirs(upload_folder, exist_ok=True)
    
    # Register blueprints
    app.register_blueprint(vision_api, url_prefix='/api')
    
    # Root route
    @app.route('/')
    def index():
        return app.send_static_file('index.html')
    
    return app