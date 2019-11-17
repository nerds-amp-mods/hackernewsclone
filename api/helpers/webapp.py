from flask import Flask, request, jsonify, url_for
from . import Storage


app = Flask(__name__)
s = Storage()

@app.before_request
def check_auth():
    pass

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, x-datatool-site'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE'
    response.headers['Access-Control-Allow-Origin'] = '*'

    return response

@app.route('/')
def index():
    return jsonify({
        'name': 'hackernewscloneapi'
    })


@app.route('/add', methods=['POST'])
def add():
    data = request.json
    if not data:
        return jsonify({}), 400
    if 'headline' not in data:
        return jsonify({'error_message': 'missing article headline in payload'}), 412
    if 'source' not in data:
        return jsonify({'error_message': 'missing article source in payload'}), 412
    if 'source_url' not in data:
        return jsonify({'error_message': 'missing source url in payload'}), 412
    if 'story_url' not in data:
        return jsonify({'error_message': 'missing story_url in payload'}), 412
    s.update(data)
    return jsonify({'message':'article added to datastore'}),201

@app.route('/news', methods=['GET', 'POST'])
def get_news():
    filters = request.json
    articles = s.fetch(filters=filters)
    return jsonify(articles)