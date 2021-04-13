from flask import request, jsonify

from app import app, API_PREFIX

from repositories import get_comments, create_comment


@app.route(f'{API_PREFIX}/posts/<int:post_id>/comments/', methods=['GET', 'POST'])
def comments_api(post_id):
    if request.method == 'POST':
        comment_data = dict(request.json or request.form)
        if not comment_data.get('content') or comment_data.get('content') == '':
            return jsonify({'message': 'Content field is required'}), 400
        create_comment_data = create_comment(post_id, comment_data)
        return jsonify(create_comment_data), 201
    comments = get_comments(post_id)
    if not comments:
        return jsonify({'message': 'Not Found'}), 404
    return jsonify(comments), 200

