import json
from .config.extentions import RedisConfig


class Publish(RedisConfig):
    def __init__(self, data, event_type):
        self.data = {
            'data': data,
            'event_type': event_type
        }
        self.publish()

    def stringify(self):
        return json.dumps(self.data)

    def publish(self):
        self.client.publish(self.CHANNEL_NAME, self.stringify())
