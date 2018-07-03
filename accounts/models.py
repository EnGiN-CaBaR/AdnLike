from django.db import models
from django.contrib.auth.models import User, Group


class City(models.Model):
    id = models.AutoField(primary_key=True)
    city_name = models.TextField(max_length=20, unique=True, verbose_name='City')
    insert_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'accounts'
        ordering = ['insert_date']

    def __str__(self):
        return self.city_name


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    country_name = models.TextField(max_length=20, unique=True, verbose_name='Country')
    insert_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'accounts'
        ordering = ['insert_date']

    def __str__(self):
        return self.country_name


class UserProfile(models.Model):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    GENDER_CHOICES = ((MALE, 'Male'),
                      (FEMALE, 'Female'))

    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    city = models.ForeignKey('accounts.City', on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey('accounts.Country', on_delete=models.SET_NULL, null=True)
    birthday = models.DateField(null=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=MALE)
    timezone = models.IntegerField(null=True)
    verified = models.NullBooleanField()

    insert_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        app_label = 'accounts'
        ordering = ['user']
