from django.shortcuts import render, redirect
from django.urls import  reverse_lazy
from django.contrib import messages
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import  get_user_model

from accounts.forms import RegistrationForm
from accounts.tasks import send_confirmation_mail
from accounts.tools.tokens import account_activation_token

User = get_user_model()


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # http://example.com
            site_address = request.is_secure() and "https://" or "http://" + request.META['HTTP_HOST']  # https
            send_confirmation_mail(user_id=user.id, site_address=site_address)
            messages.success(request, 'Siz ugurla qeydiyyatdan kecdiniz')
            return redirect(reverse_lazy('stories:index'))
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Email is activated')
        return redirect(reverse_lazy('stories:index'))
    elif user:
        messages.error(request, 'Email is not activated. May be is already activated')
        return redirect(reverse_lazy('accounts:register'))
    else:
        messages.error(request, 'Email is not activated')
        return redirect(reverse_lazy('accounts:register'))
