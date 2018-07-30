from django.forms import ModelForm
from advertisement.models import AdvSummary
from django.utils.translation import ugettext_lazy as _
import datetime
from django import forms


class AdvertisementSoftForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control form-control-lg', 'placeholder': 'Advertisement Name', 'autocomplete': 'off'})
        self.fields['budget'].widget.attrs.update(
            {'class': 'form-control form-control-lg', 'placeholder': 'Advertisement Budget', 'autocomplete': 'off'})
        self.fields['max_fee_per_like'].widget.attrs.update(
            {'class': 'form-control form-control-lg', 'placeholder': 'Advertisement Max Fee Per Like',
             'autocomplete': 'off'})
        self.fields['expire_date'].widget.attrs.update({'class': 'form-control form-control-lg', 'autocomplete': 'off'})

    class Meta:
        model = AdvSummary
        fields = ['name', 'budget', 'max_fee_per_like', 'expire_date']

    def clean_expire_date(self):
        data = self.cleaned_data['expire_date']

        if data < datetime.date.today():
            raise forms.ValidationError(_('Invalid Date - Expire Date must be bigger than Today'))

        return data