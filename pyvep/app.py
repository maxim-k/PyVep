
import flask
from flask.ext.cors import CORS
from pyvep.config import config

app = flask.Flask(__name__)
CORS(app)
base_url = config('base_url')


@app.route(base_url, methods=['GET'])
def hello_world():
    return ""


@app.route(base_url, methods=['POST'])
def api():
    print(type(flask.request.get_json(force=True)))
    genelist = flask.request.get_json(force=True)
    return flask.jsonify(get_synonyms(genelist))

if __name__ == '__main__':
    app.run()

