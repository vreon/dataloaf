from urlparse import urljoin
import json
from flask import Flask, request, make_response, jsonify, abort, url_for, \
    escape
from dataloaf import Grammar
import os

app = Flask(__name__)

# Endpoints are loaded at app start
GMR_ROOT = os.path.join(os.path.dirname(__file__), 'gmr')
GRAMMARS = [fn[:-4] for fn in os.listdir(GMR_ROOT) if fn.endswith('.gmr')]


def jsonify_plain(*args, **kwargs):
    response = jsonify(*args, **kwargs)
    if 'application/json' not in request.headers.get('accept', ''):
        response.mimetype = 'text/plain'
    return response


def jsonpify_plain(**kwargs):
    callback = escape(request.args.get('callback', 'dataloaf'))
    payload = json.dumps(**kwargs)
    wrapped = '%s(%s)' % (callback, payload)

    response = make_response(wrapped)
    if 'application/json' in request.headers.get('accept', ''):
        response.mimetype = 'application/json'
    else:
        response.mimetype = 'text/plain'

    return response


@app.route('/')
def index():
    description = (
        'Data Loaf is a web service that spews out random structured data.'
    )
    parameters = [{'name': 'count', 'type': 'integer', 'required': False}]
    example = urljoin(
        request.url_root,
        url_for('render', name='names', count='10')
    )
    changelog = {'2011-06-02': 'Added support for JSONP requests.'}

    return jsonify_plain(
        description=description,
        example=example,
        endpoints=['/' + s for s in GRAMMARS],
        parameters=parameters,
        changelog=changelog
    )


@app.route('/<name>')
def render(name):
    if name in GRAMMARS:
        with open(os.path.join(GMR_ROOT, name + '.gmr')) as f:
            grammar = Grammar(f.read())
    else:
        abort(404)

    count = min(max(request.args.get('count', 1, type=int), 1), 100)
    results = [grammar.walk() for i in range(count)]

    if 'callback' in request.args:
        return jsonpify_plain(results=results)

    return jsonify_plain(results=results)


if __name__ == "__main__":
    app.run(debug=True)
