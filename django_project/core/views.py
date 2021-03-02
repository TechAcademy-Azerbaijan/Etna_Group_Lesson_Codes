from django.shortcuts import render
from django.http import Http404
from django.views.generic import TemplateView


# class HomeView(TemplateView):
#     template_name = 'index.html'


def home(request):
    return render(request, 'index.html')


def about(request, user_id):
    user_list = [
        {
            'id': 1,
            'full_name': 'Yusif Huseynli'
        },
        {
            'id': 2,
            'full_name': 'Emrah Bagirov'
        }
    ]
    try:
        user_data = next(filter(lambda user: user['id'] == user_id, user_list))
    except:
        raise Http404
    context = {
        'user_info': user_data
    }
    return render(request, 'about.html', context)
