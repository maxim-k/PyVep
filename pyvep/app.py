import glob
import os

from flask import Flask, flash, render_template, request, redirect, url_for, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename

from pyvep.config import config
from pyvep.vep import run, run_dev


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = config('pyvep_uploads')
app.config['ALLOWED_EXTENSIONS'] = {'vcf', 'txt'}

CORS(app)
init_url = config('init_url')
pyvep_results = config('pyvep_results')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('/Users/maximkuleshov/PycharmProjects' + app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
        return None
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('selector.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route(init_url, methods=['GET'])
def run_vep():
    files_path = os.path.join(app.config['UPLOAD_FOLDER'], '*')
    # TODO: return a decent file, not the last one
    file = os.path.abspath(sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)[0])
    res_file = os.path.basename(run('homo_sapiens', 'GRCh38', file))
    return send_from_directory(pyvep_results, '{}.txt'.format(res_file))


@app.route('{}/dev'.format(init_url), methods=['GET'])
def run_vep_dev():
    files_path = os.path.join(app.config['UPLOAD_FOLDER'], '*')
    # TODO: return a decent file, not the last one
    file = os.path.abspath(sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)[0])
    res_file = os.path.basename(run_dev('homo_sapiens', 'GRCh38', file))
    return send_from_directory(pyvep_results, '{}.txt'.format(res_file))


if __name__ == '__main__':
    app.run()

