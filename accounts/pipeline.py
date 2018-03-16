from django.contrib.auth.models import Group
from social_core.exceptions import AuthFailed


def add_user_to_group(backend, user=None, *args, **kwargs):
    if not user:
        return

    user_request_type = backend.strategy.session_get('key')
    influencer = Group.objects.get_by_natural_key(name='influencer')
    brand = Group.objects.get_by_natural_key(name='brand')
    is_user_has_group = user.groups.all().exists()

    if not is_user_has_group:
        if user_request_type == 'influencer' and influencer:
            influencer.user_set.add(user)
        elif user_request_type == 'brand' and brand:
            brand.user_set.add(user)
        else:
            return
    else:
        user_group = [g.name for g in user.groups.all()]
        if user_request_type != user_group[0]:
            msg = 'This account is already in use as {0}. Please login as different user type'.format(user_group[0])
            raise AuthFailed(backend, msg)
        else:
            return
