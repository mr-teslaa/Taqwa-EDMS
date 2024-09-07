import os
import uuid
from config import Config
from flask import current_app

def save_file(file, folder=Config.UPLOAD_FOLDER):
    # Generate a random filename
    filename = generate_random_filename(file.filename)
    file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], folder, filename)
    
    # Save the file
    file.save(file_path)
    return file_path

def generate_random_filename(filename):
    # Extract the file extension
    ext = filename.rsplit('.', 1)[1].lower()
    # Generate a random filename with the extension
    random_filename = f"{uuid.uuid4().hex}.{ext}"
    return random_filename
