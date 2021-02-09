from ez_django.mailers import Mailer 

class AccountMailer(Mailer):
    """AccountMailer sends mail for for all account functionality."""

    def account_confirmation_email(self, account):
        self.template = "accounts/mail/account_confirmation_email.html"
        self.subject = "Account Confirmation"
        self.to = [account.email]
        self.context["account"] = account
        self.send_mail()