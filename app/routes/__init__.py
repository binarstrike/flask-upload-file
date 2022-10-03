from flask import Flask
import os

root_dir = f"{os.path.dirname(os.path.abspath(__file__))}/.."

flask_main = Flask(__name__, root_path=root_dir)

flask_main.config['UPLOAD FOLDER'] = f"{root_dir}/../uploaded-file"

from . import upload
