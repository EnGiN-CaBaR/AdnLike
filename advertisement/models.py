from django.db import models


class Advertisement(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.ForeignKey('advertisement.Brand')
    categories = models.ManyToManyField('advertisement:Category')
    name = models.CharField(max_length=255, null=False)
    budget = models.DecimalField(max_digits=38, decimal_places=9, null=False)
    max_fee_per_like = models.IntegerField(null=False)
    expire_date = models.DateField(null=False)
    adv_image = models.ImageField(upload_to='adv_image/')
    adv_desc = models.CharField(max_length=255, null=False)
    adv_min_follower = models.IntegerField(null=False)
    adv_max_follower = models.IntegerField(null=False)

    insert_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_date = models.DateTimeField(auto_now=True)


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)

    insert_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_date = models.DateTimeField(auto_now=True)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)

    insert_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_date = models.DateTimeField(auto_now=True)
