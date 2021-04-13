import random
import requests

post_list = [
    {
        'id': 1,
        'title': 'Blog 1'
    },
    {
        'id': 2,
        'title': 'Blog 2'
    },
    {
        'id': 3,
        'title': 'Blog 3'
    }
]


def get_posts():
    return post_list


def create_post(post_data):
    post_id = random.randint(1, 100)
    post_data['id'] = post_id
    post_list.append(post_data)
    data = {
        'event_type': 'PostCreated',
        'data': post_data,
    }
    requests.post('http://localhost:5005/events/', json=data)
    return post_data
