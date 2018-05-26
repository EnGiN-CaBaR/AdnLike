from django.db import models


class AdvSummary(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.ForeignKey('advertisement.Brand', on_delete=models.SET_NULL, null=True)
    categories = models.ManyToManyField('advertisement.Category')
    name = models.CharField(max_length=255, null=False)
    budget = models.DecimalField(max_digits=38, decimal_places=2, null=False)
    max_fee_per_like = models.IntegerField(null=False)
    expire_date = models.DateField(null=False)
    adv_image = models.ImageField(upload_to='adv_image/')
    adv_desc = models.CharField(max_length=255, null=False)
    adv_min_follower = models.IntegerField(null=False)
    adv_max_follower = models.IntegerField(null=False)
    is_approved = models.BooleanField(null=False)

    insert_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)

    insert_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)

    insert_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
