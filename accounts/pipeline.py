from django.contrib.auth.models import Group
from social_core.exceptions import AuthFailed
from accounts.models import Country, City, UserProfile
import datetime


def add_user_to_group(backend, user=None, is_new=True, *args, **kwargs):
    if user and not is_new:
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


def populate_location(response, details, user=None, *args, **kwargs):
    city, country = map(str.capitalize, map(str.strip, response.get('location', '').get('name', '').split(',')))
    city_object = City.objects.get_or_create(city_name=city)
    country_object = Country.objects.get_or_create(country_name=country)

    return {
        'details': {'city': city_object, 'country': country_object}
    }


def populate_user_profile(backend, details, response, user=None, *args, **kwargs):
    city = details.get('city', '')[0]
    country = details.get('country', '')[0]
    birthday = datetime.datetime.strptime(response.get('birthday', ''), '%m/%d/%Y').strftime('%Y-%m-%d')
    gender = response.get('gender', '')
    timezone = response.get('timezone', '')
    verified = response.get('verified', '')

    up = UserProfile.objects.update_or_create(user=user, city=city, country=country, birthday=birthday, gender=gender,
                                              timezone=timezone, verified=verified)

    return {
        'details': {'is_profile_created': up[1]}
    }
