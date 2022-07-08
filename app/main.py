from flask import Blueprint, flash, redirect, url_for
from flask import request
from flask import current_app 
from flask import render_template
import os 
from . import audio_fingerprinting 
from werkzeug.utils import secure_filename

bp = Blueprint('main', __name__)


@bp.post('/create_fingerprint')
def create_fingerprint():
    file = request.files["audio"]
    filename = secure_filename(file.filename)
    file.save(os.path.join(current_app.config["UPLOADS_FOLDER"], filename))
    saved = audio_fingerprinting.create_audio_fingerprint(os.path.join(current_app.config['UPLOADS_FOLDER'], filename)) 
    flash("fingerprint created" if saved else "fingerprint exists")
    return render_template('index.html', saved=saved)


@bp.get('/') 
def home():
    return render_template('index.html')
    

@bp.post('/match_fingerprint')
def match():
    file = request.files["audio"]
    filename = secure_filename(file.filename)
    file.save(os.path.join(current_app.config["UPLOADS_FOLDER"], filename))
    matches = audio_fingerprinting.find_audio(os.path.join(current_app.config['UPLOADS_FOLDER'], filename)) 
    return render_template('index.html', matches=matches)