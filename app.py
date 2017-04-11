import os
import glob

from flask import Flask, render_template, request, redirect, url_for, send_from_directory, safe_join
from flask_cors import CORS
from werkzeug.utils import secure_filename
from config import config

from vep import run, vep_homedir

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'vcf', 'txt'}

CORS(app)
init_url = config('init_url')
api_url = config('api_url')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/')
def index():
    return render_template('index.html')


# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        return redirect(url_for('uploaded_file', filename=filename))

# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
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

