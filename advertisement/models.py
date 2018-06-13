import uuid

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

User = get_user_model()


def user_directory_path(instance, filename):
    my_custom_date = timezone.now().date()
    return 'advertisement_image/{0}/user_{1}/{2}'.format(my_custom_date, instance.username.id, filename)


class AdvSummary(models.Model):
    id = models.AutoField(primary_key=True)
    guid = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    categories = models.ManyToManyField('advertisement.Category')
    name = models.CharField(max_length=255)
    adv_slug_name = models.SlugField(allow_unicode=True, unique=True, null=True)
    brand_slug_name = models.SlugField(allow_unicode=True, unique=True, null=True)
    budget = models.DecimalField(max_digits=38, decimal_places=2)
    max_fee_per_like = models.IntegerField()
    expire_date = models.DateField()
    advertisement_image = models.ImageField(upload_to=user_directory_path,
                                            verbose_name='Advertisement Image',
                                            null=True, blank=True)
    adv_desc = models.CharField(max_length=255, verbose_name='Advertisement Description', null=True)
    adv_min_follower = models.IntegerField(verbose_name='Advertisement Minimum Follower', null=True)
    adv_max_follower = models.IntegerField(verbose_name='Advertisement Maximum Follower', null=True)
    is_approved = models.BooleanField(null=False, default=0)

    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'advertisement_summary'
        ordering = ['-publish_date']

    def __str__(self):
        return self.name

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('advertisement:publish', kwargs={'adv_slug_name': self.adv_slug_name,
                                                        'pk': self.pk})


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)

    insert_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    username = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    insert_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
