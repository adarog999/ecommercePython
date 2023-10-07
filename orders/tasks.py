from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task

def order_created(order_id):

    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name}, \n\n'\
                f'You Have SuccessFully placed an order' \
                f'Your\'e order ID is {order.id}'

    mail_sent = send_mail(subject,message,'bobbisky5@gmail.com',[order.email])

    return mail_sent