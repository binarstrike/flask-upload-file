from crypt import methods
import os
from . import flask_main as me
from flask import render_template as rt
from flask import request, flash, redirect
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'txt','pdf','jpg','jpeg','gif','png'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@me.route("/upload", methods=["POST","GET"])
def upload_endpoint():
    if request.method == "POST":
        if 'file' not in request.files:
            flash("no file part")
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('tidak ada file yang dipilih')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(me.config['UPLOAD FOLDER'], filename))
            return {"data":"upload file success"}
        elif file and not allowed_file(file.filename):
            return {"data":f"upload file fail, check internet connection or file extension disallowed. Allowed file extension {ALLOWED_EXTENSIONS}"}
    else: return rt("upload.html")