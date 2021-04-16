import time
import datetime
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from django.core.mail import EmailMessage
from django.conf import settings

from celery import shared_task

from stories.models import Subscriber, Recipe


@shared_task
def dump_database():
    print('dump process started')
    time.sleep(30)
    print('dump process finished')


@shared_task
def send_mail_to_subscribers():
    user_emails = Subscriber.objects.filter(is_active=True).\
        values_list('email', flat=True)
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    today = datetime.date.today()
    recipes = Recipe.objects.filter(is_published=True, created_at__range=[yesterday, today])
    subject = _('Latest popular post for you')
    context = {
        'recipes': recipes,
        'SITE_ADDRESS': settings.SITE_ADDRESS,
    }
    body = render_to_string('emails/email-subscribers.html', context)

    mail = EmailMessage(subject, to=user_emails, from_email=settings.EMAIL_HOST_USER, body=body)
    mail.content_subtype = 'html'
    mail.send(fail_silently=True)
