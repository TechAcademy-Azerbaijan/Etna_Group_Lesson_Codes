from http import HTTPStatus

from flask import request, send_from_directory, jsonify, abort
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError

from ..api import api
from ..config.base import MEDIA_ROOT
from ..models import *
from ..schemas.schema import CommentSchema


@api.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(MEDIA_ROOT, filename)


@api.route('/posts/<int:post_id>/comments/', methods=['GET', 'POST'])
# @jwt_required()
def comments(post_id):
    if request.method == 'POST':
        try:
            data = dict(request.json or request.form)
            serializer = CommentSchema().load(data)
            print(serializer)
            content = serializer.get('content')
            parent_comment = serializer.get('parent_comment')
            user_id = 1
            comment = Comment(content=content, user_id=user_id, post_id=post_id)
            comment.save()
            print(parent_comment)
            parent_comment = Comment.objects.filter(post_id=post_id, id=parent_comment).first()
            while True:
                print(parent_comment is None)

                parent_comment = Comment.objects.filter(post_id=post_id, id=parent_comment.id).first()
                comment_dict = CommentSchema().dump(comment)
                parent_comment.comments.append(comment_dict)
                parent_comment.save()
                if not Comment.objects.filter(post_id=post_id, id=parent_comment.id):
                    break
            return CommentSchema().jsonify(parent_comment), HTTPStatus.CREATED
        except ValidationError as err:
            return jsonify(err.messages), HTTPStatus.BAD_REQUEST
    comments = Comment.objects.filter(post_id=post_id)
    if not comments:
        return abort(404)
    return CommentSchema().jsonify(comments, many=True), HTTPStatus.OK

