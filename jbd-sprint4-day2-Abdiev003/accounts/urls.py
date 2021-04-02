from django.urls import path, re_path

from accounts.views import register, activate, login, logout, change_password, UserProfileView, UserEditProfileView

app_name = 'accounts'

urlpatterns = [
    path('register/', register, name='register'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,33})/$',
            activate, name='activate'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('change-password/', change_password, name='change_password'),
    path('user-profile/<int:pk>/', UserProfileView.as_view(), name='user_profile'),
    path('edit-profile/', UserEditProfileView.as_view(), name='edit_profile'),
]
