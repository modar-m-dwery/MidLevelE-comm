from six import text_type
from django.contrib.auth.token import PasswordResetTokenGenerator

class TokenGenerator(PasswordResetTokenGenerator):
    def make_hash_value(self,user,timestamp):
        return ( text_type(user.pk)+text_type(timestamp))
generate_token = TokenGenerator()