from flask import Blueprint, request, jsonify
import os
from werkzeug.utils import secure_filename
from app.services.openai_service import OpenAIService

vision_api = Blueprint('vision_api', __name__)
openai_service = OpenAIService()

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@vision_api.route('/analyze', methods=['POST'])
def analyze_image():
    # Check if the post request has the file part
    if 'image' not in request.files:
        return jsonify({'success': False, 'error': 'No image part in the request'}), 400
    
    file = request.files['image']
    
    # If user does not select file, browser might send empty file without filename
    if file.filename == '':
        return jsonify({'success': False, 'error': 'No image selected'}), 400
    
    if file and allowed_file(file.filename):
        # Read the file content directly
        image_data = file.read()
        
        # Get optional prompt or use default
        prompt = request.form.get('prompt', "Please describe in french this image in detail. What do you see?")
        
        # Analyze image
        result = openai_service.analyze_image(image_data, prompt)
        
        if result['success']:
            return jsonify(result), 200
        else:
            return jsonify(result), 500
    
    return jsonify({'success': False, 'error': 'File type not allowed'}), 400