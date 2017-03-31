
import flask
from flask.ext.cors import CORS
from pyvep.config import config
from pyvep.vep import vep

app = flask.Flask(__name__)
CORS(app)
init_url = config('init_url')
base_url = config('base_url')


@app.route(init_url, methods=['GET'])
def download_ref():
    return ""


@app.route(base_url, methods=['POST'])
def api():
    print(type(flask.request.get_json(force=True)))
    genelist = flask.request.get_json(force=True)
    return flask.jsonify()

if __name__ == '__main__':
    app.run()

