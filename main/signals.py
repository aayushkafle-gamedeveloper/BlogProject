from django.db.models.signals import post_save
from django.dispatch import receiver
from main.models import Blog, Subscriber
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=Blog)
def send_email(sender, instance, **kwargs):
    print("-----------------------------------------------------------")
    subscribers = Subscriber.objects.all()
    mail_to = [subscriber.email for subscriber in subscribers]
    send_mail(
        instance.title,
        instance.intro,
        settings.EMAIL_HOST_USER,
        mail_to,
        fail_silently=False,
    )

