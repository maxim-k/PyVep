import glob
import os

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename

from pyvep.config import config
from pyvep.vep import run, vep_homedir

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'vcf', 'txt'}

CORS(app)
init_url = config('init_url')
api_url = config('api_url')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file', filename=filename))


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route(init_url, methods=['GET'])
def run_vep():
    files_path = os.path.join(app.config['UPLOAD_FOLDER'], '*')
    file = os.path.abspath(sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)[0])
    run('homo_sapiens', 'GRCh38', file)
    return send_from_directory(vep_homedir, '{}.txt'.format(file))


@app.route(api_url, methods=['POST'])
def api():
    return None

if __name__ == '__main__':
    app.run()

