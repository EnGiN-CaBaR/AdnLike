from social_django.middleware import SocialAuthExceptionMiddleware
from social_core.exceptions import AuthAlreadyAssociated
import six


class SocialAuthLoginExceptionMiddleware(SocialAuthExceptionMiddleware):

    def get_message(self, request, exception):
        if isinstance(exception, AuthAlreadyAssociated):
            return exception.args[0]
        else:
            return six.text_type(exception)
