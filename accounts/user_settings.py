from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
from social_core.exceptions import AuthFailed
from accounts.models import Country, City, UserProfile


def add_user_to_group(user, is_new, user_group):
    if user and not is_new:
        return

    influencer = Group.objects.get_by_natural_key(name='influencer')
    brand = Group.objects.get_by_natural_key(name='brand')
    is_user_has_group = user.groups.all().exists()

    if not is_user_has_group:
        if user_group == 'influencer' and influencer:
            influencer.user_set.add(user)
        elif user_group == 'brand' and brand:
            brand.user_set.add(user)
        else:
            return
    else:
        user_group = [g.name for g in user.groups.all()]
        if user_group != user_group[0]:
            raise AuthFailed()
        else:
            return


def populate_city(city):
    city_object = City.objects.get_or_create(city_name=city)
    return city_object


def populate_country(country):
    country_object = Country.objects.get_or_create(country_name=country)
    return country_object


def populate_user_profile(user, city='', country='', birthday='1900-01-01', gender='', timezone=-1, verified=False):
    user_profile = UserProfile.objects.filter(user_id__exact=user)
    if user_profile.exists():
        up = user_profile.update(user=user, city=city, country=country,
                                 birthday=birthday, gender=gender,
                                 timezone=timezone, verified=verified)
    else:
        up = UserProfile.objects.create(user=user, city=city, country=country,
                                        birthday=birthday, gender=gender,
                                        timezone=timezone, verified=verified)

    return up
