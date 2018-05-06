from django.contrib import admin
from accounts.models import City, Country, UserProfile

# Register your models here.

admin.site.register(City)
admin.site.register(Country)
admin.site.register(UserProfile)
