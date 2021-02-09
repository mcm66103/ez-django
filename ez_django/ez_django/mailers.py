from django.core.mail import send_mail
from django.template.loader import render_to_string

class Mailer():

    def __init__(self, *args, **kwargs):
        self.from_email = "test@test.com"

    def send_mail(self):
        html_message = render_to_string(self.template, self.context)
        send_mail(
            self.subject, 
            None, # plain text message
            self.from_email,
            self.to,
            html_message = html_message
        )