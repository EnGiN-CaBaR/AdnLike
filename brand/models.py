from django.db import models
from django.contrib.auth import get_user_model
from advertisement.models import AdvSummary

User = get_user_model()


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    username = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    insert_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name