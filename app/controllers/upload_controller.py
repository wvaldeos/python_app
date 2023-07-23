from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from app import app
from app.models.pdf_model import extract_text
import os
from app.models.process_pdf import extract_data

@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    text = extract_text(filename)
    json_result = extract_data(text)
    return json_result
