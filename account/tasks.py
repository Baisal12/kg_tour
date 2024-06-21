from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from celery import shared_task

@shared_task
def send_activation_code(email, activation_code):
    context = {
        'text_detail':'Спасибо за регистратцию!',
        'email':email,
        'domain':'http://localhost:800',
        'activation_code':activation_code
    }
    msg_html = render_to_string('email.html', context)
    massage = strip_tags(msg_html)

    send_mail(
        'Account Activation',
        massage,
        'admin@admin.com',
        [email],
        html_message=msg_html,
        fail_silently=True
    )