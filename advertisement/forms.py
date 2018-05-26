from django.forms import ModelForm
from advertisement.models import AdvertisementSummary
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime


class AdvertisementForm(ModelForm):
    class Meta:
        model = AdvertisementSummary
        fields = ['name', 'budget', 'max_fee_per_like', 'expire_date']

    def clean_expire_date(self):
        data = self.cleaned_data['expire_date']

        if data < datetime.date.today():
            raise ValidationError(_('Invalid Date - Expire Date must be bigger than Today'))

        return data
