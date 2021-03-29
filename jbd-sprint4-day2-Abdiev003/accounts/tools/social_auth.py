

def update_user_social_data(strategy, *args, **kwargs):
    response = kwargs['response']
    user = kwargs['user']
    if user.image:
        return None
    picture = response.get('picture')
    user.image = picture
    user.save()