from social_core.exceptions import AuthFailed
import datetime
from accounts import user_settings


def social_auth_add_user_to_group(backend, user=None, is_new=True, *args, **kwargs):
    try:
        user_group = backend.strategy.session_get('key')
        user_settings.add_user_to_group(user, is_new, user_group)
    except AuthFailed:
        msg = 'This account is already in use as {0}. Please login as different user type'.format(user_group[0])
        raise AuthFailed(backend, msg)


def social_auth_populate_location(response, details, user=None, *args, **kwargs):
    city, country = map(str.capitalize, map(str.strip, response.get('location', '').get('name', '').split(',')))
    return {
        'details': {'city': user_settings.populate_city(city), 'country': user_settings.populate_country(country)}
    }


def social_auth_populate_user_profile(backend, details, response, user=None, *args, **kwargs):
    city = details.get('city', '')[0]
    country = details.get('country', '')[0]
    birthday = datetime.datetime.strptime(response.get('birthday', ''), '%m/%d/%Y').strftime('%Y-%m-%d')
    gender = response.get('gender', '')
    timezone = response.get('timezone', '')
    verified = response.get('verified', '')

    up = user_settings.populate_user_profile(user, city, country, birthday, gender, timezone, verified)

    return {
        'details': {'is_profile_created': up[1]}
    }
