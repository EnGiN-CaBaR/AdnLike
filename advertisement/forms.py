from django.forms import ModelForm
from advertisement.models import Advertisement


class AdvertisementForm(ModelForm):
    class Meta:
        model = Advertisement
        fields = ['name', 'budget', 'max_fee_per_like', 'expire_date']
