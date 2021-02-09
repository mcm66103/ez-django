from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

class Mailer():

    def __init__(self, context = {}):
        self.from_email = "test@test.com"
        self.context = context
        self.context["BASE_URL"] = settings.BASE_URL

    def send_mail(self):
        html_message = render_to_string(self.template, self.context)
        send_mail(
            self.subject, 
            None, # plain text message
            self.from_email,
            self.to,
            html_message = html_message
        )