from flask import request, jsonify

from app import app, API_PREFIX

from repositories import get_posts, create_comment, create_post


@app.route(f'{API_PREFIX}/posts/', methods=['GET', 'POST'])
def all_posts():
    comments = get_posts()
    return jsonify(comments), 200


@app.route('/events/', methods=['POST',])
def events():
    data = dict(request.form or request.json)
    action_data = data.get('data')
    print('action_data', action_data)
    if data.get('event_type') == 'PostCreated':
        create_post(action_data)
    if data.get('event_type') == 'CommentCreated':
        pass
    return jsonify({'message': 'success'})

