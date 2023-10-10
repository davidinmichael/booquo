from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from email.message import EmailMessage
import smtplib
import ssl


def send_emails(receiver, username):
    sender = "davidinmichael@gmail.com"
    password = "trplzetkubdspzuq"

    subject = "Daily Quotes"
    context = ssl.create_default_context()

    obj = EmailMessage()
    obj["From"] = sender
    obj["To"] = receiver
    obj["subject"] = subject
    obj.set_content(f"Welcome to the daily quotes, we are glad to have you.\n- David Michael")
    obj.add_alternative(
        f"""
    <!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body style="background-color: #311b92; font-family: Arial, sans-serif; color: #ffffff; text-align: center;">
    <div style="background-color: #673ab7; padding: 20px;">
        <h1 style="color: #ffffff;">Welcome {username}</h1>
    </div>
    <div style="padding: 20px;">
        <p>Welcome to the daily quotes, we are glad to have you.</p>
        <p>- David Michael</p>
    </div>
    <div style="padding: 20px;">
        <a href="https://twitter.com/davidinmichael" style="background-color: #673ab7; color: #ffffff; text-decoration: none; padding: 10px 20px; border-radius: 5px; margin-right: 10px;">Twitter</a>
        <a href="https://linkedin.com/in/davidinmichael" style="color: #ffffff; text-decoration: none;">Linkedin</a>
    </div>
</body>
</html>
""", subtype="html")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, obj.as_string())

@receiver(post_save, sender=User)
def welcome_email(sender, instance, created, **kwargs):
    if created:
        send_emails(instance.email, instance.username)