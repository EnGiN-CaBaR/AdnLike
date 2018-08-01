from django.db import models
from django.contrib.auth import get_user_model
from advertisement.models import AdvSummary

User = get_user_model()


class InfluencerSummary(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    trx = models.ForeignKey('influencer.AdvTrx', on_delete=models.CASCADE)
    registered_Adv = models.ManyToManyField('advertisement.AdvSummary')

    insert_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_date = models.DateTimeField(auto_now=True)


class AdvTrx(models.Model):
    id = models.AutoField(primary_key=True)

    insert_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_date = models.DateTimeField(auto_now=True)
