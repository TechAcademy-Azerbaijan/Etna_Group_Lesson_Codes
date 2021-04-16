from ..config.extentions import ma
from flask_marshmallow.fields import AbsoluteURLFor
from marshmallow import validates, ValidationError, fields, validate

from ..models import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    image = AbsoluteURLFor(
        'uploaded_file',
        filename='<image>'
    )
    password = ma.String(load_only=True, required=True, validate=[validate.Length(min=8, max=20)])
    email = fields.Email(required=True, unique=True, validate=[validate.Length(min=7),])

    class Meta:
        model = User
        include_fk = True
        load_instance = True

    @validates('email')
    def validate_email(self, value):
        if User.query.filter_by(email=value).first():
            raise ValidationError("Email field must be unique!")
        return True

