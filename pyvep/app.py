
import flask
from flask_cors import CORS
from pyvep.config import config
from pyvep.vep import download

app = flask.Flask(__name__)
CORS(app)
init_url = config('init_url')
base_url = config('base_url')


@app.route(init_url, methods=['GET'])
def download_ref():
    download('homo_sapiens', 'GRCh38')
    return 'Downloading reference'


@app.route(base_url, methods=['POST'])
def api():
    return None

if __name__ == '__main__':
    app.run()

