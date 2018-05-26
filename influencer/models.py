from django.db import models


class InfluencerSummary(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    trx = models.ForeignKey('influencer.AdvTrx', on_delete=models.CASCADE)

    insert_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_date = models.DateTimeField(auto_now=True)


class AdvTrx(models.Model):
    id = models.AutoField(primary_key=True)

    insert_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_date = models.DateTimeField(auto_now=True)
