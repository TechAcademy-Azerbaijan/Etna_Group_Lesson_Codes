from flask import request, jsonify

from app import app, API_PREFIX

from repositories import get_posts, create_post


@app.route(f'{API_PREFIX}/posts/', methods=['GET', 'POST'])
def posts_api():
    if request.method == 'POST':
        post_data = dict(request.json or request.form)
        if not post_data.get('title') or post_data.get('title') == '':
            return jsonify({'message': 'Title field is required'}), 400
        post_create_data = create_post(post_data)
        return jsonify(post_create_data), 201
    post_list = get_posts()
    return jsonify(post_list), 200
