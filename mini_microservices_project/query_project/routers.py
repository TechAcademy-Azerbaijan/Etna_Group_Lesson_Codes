from flask import request, jsonify

from app import app, API_PREFIX

from repositories import get_posts, create_comment


@app.route(f'{API_PREFIX}/posts/', methods=['GET', 'POST'])
def all_posts():
    comments = get_posts()
    return jsonify(comments), 200

