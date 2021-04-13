import random

post_comment_list = [
    {
        'id': 1,
        'title': 'Blog 1',
        'comments': [
            {
                'id': 1,
                'content': 'Bu yaxsi postdu'
            },
            {
                'id': 2,
                'content': 'pis deyil'
            },
        ]
    },
    {
        'id': 2,
        'title': 'Blog 2',
        'comments': [
            {
                'id': 1,
                'content': 'Bu pis postdu'
            },
            {
                'id': 2,
                'content': 'yaxsi deyil'
            },
            {
                'id': 3,
                'content': 'yaxsi deyil'
            },
        ]
    },
    {
        'id': 3,
        'title': 'Blog 3',
        'comments': [
            {
                'id': 1,
                'content': 'Bu pis postdu'
            },
            {
                'id': 2,
                'content': 'yaxsi deyil'
            },
        ]
    },

]


def get_posts():
    return post_comment_list
    # return filter(lambda post_comment: post_comment['id'] == post_id, post_comment_list)


def create_comment(post_id, comment_data):
    comment_data['id'] = random.randint(1, 1000)
    for post_comments in post_comment_list:
        if post_comments['id'] == post_id:
            post_comments.setdefault('comments', [])
            post_comments['comments'].append(comment_data)
            break
    else:
        new_post = {
            'id': post_id,
            'comments': [
                comment_data
            ]
        }
        post_comment_list.append(new_post)

    return comment_data
