from http import HTTPStatus

from flask import request, send_from_directory, jsonify
from marshmallow.exceptions import ValidationError

from ..app import app
from ..models import Subscriber
from ..schemas.schema import SubscriberSchema


@app.route('/subscribe/', methods=['POST'])
def subscribe():
    data = dict(request.json or request.form)
    try:
        subscriber = SubscriberSchema().load(data)
    except ValidationError as err:
        return err.messages, 400
    subscriber.save()
    return SubscriberSchema().jsonify(subscriber), HTTPStatus.CREATED


