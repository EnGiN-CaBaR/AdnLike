from django.forms import ModelForm, CheckboxSelectMultiple, Textarea
from advertisement.models import AdvSummary
from django.utils.translation import ugettext_lazy as _
import datetime
from django import forms


class AdvertisementSoftForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control form-control-lg', 'placeholder': 'Advertisement Name'})
        self.fields['budget'].widget.attrs.update(
            {'class': 'form-control form-control-lg', 'placeholder': 'Advertisement Budget'})
        self.fields['max_fee_per_like'].widget.attrs.update(
            {'class': 'form-control form-control-lg', 'placeholder': 'Advertisement Max Fee Per Like'})
        self.fields['expire_date'].widget.attrs.update({'class': 'form-control form-control-lg'})

    class Meta:
        model = AdvSummary
        fields = ['name', 'budget', 'max_fee_per_like', 'expire_date']

    def clean_expire_date(self):
        data = self.cleaned_data['expire_date']

        if data < datetime.date.today():
            raise forms.ValidationError(_('Invalid Date - Expire Date must be bigger than Today'))

        return data


class AdvertisementDetailForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = AdvSummary
        exclude = ['brand', 'name', 'budget', 'max_fee_per_like', 'expire_date', 'is_approved']
        widgets = {'categories': CheckboxSelectMultiple(), 'adv_desc': Textarea()}
