from ..config.extentions import ma
from flask_marshmallow.fields import AbsoluteURLFor
from marshmallow import validates, ValidationError, fields, validate


from ..models import Comment


class CommentSchema(ma.Schema):
    id = fields.String(dump_only=True)
    post_id = fields.Integer(dump_only=True)
    user_id = fields.Integer(dump_only=True)
    content = fields.String(required=True, validate=[validate.Length(min=1, max=255)])
    parent_comment = fields.String(load_only=True)
    comments = fields.Method("get_comments")

    def get_comments(self, obj):
        print(obj.comments)
        return obj.comments
