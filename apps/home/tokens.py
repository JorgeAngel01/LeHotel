from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six  

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, reserva, timestamp):
        return (
            six.text_type(reserva.pk) + six.text_type(timestamp)
        )

account_activation_token = AccountActivationTokenGenerator()