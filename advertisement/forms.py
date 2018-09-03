from django.forms import ModelForm, Textarea
from advertisement.models import AdvSummary, Category, AdvImages
from django.utils.translation import ugettext_lazy as _
import datetime
from django import forms
import re


class AdvertisementImageForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['advertisement_image'].widget.attrs.update(
            {'class': 'custom-file-input'})
        self.fields['advertisement_image'].required = False

    class Meta:
        model = AdvImages
        exclude = ['summary']
        help_texts = {'advertisement_image': _('Image for Advertisement')}


class AdvertisementDetailForm(ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(),
                                                help_text='Advertisement Categories. It is multiple choice field')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categories'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['adv_min_follower'].widget.attrs.update(
            {'class': 'form-control form-control-lg', 'placeholder': '0'})
        self.fields['adv_max_follower'].widget.attrs.update(
            {'class': 'form-control form-control-lg', 'placeholder': '10000'})
        self.fields['adv_desc'].widget.attrs.update(
            {'class': 'form-control form-control-lg', 'placeholder': 'Descriptions #Hashtags'})

    class Meta:
        model = AdvSummary
        exclude = ['brand', 'name', 'budget', 'max_fee_per_like', 'expire_date', 'is_approved', 'username',
                   'create_date', 'publish_date', 'slug_name', 'brand_slug_name', 'guid']
        widgets = {'adv_desc': Textarea(attrs={'width': '450', 'height': '100', 'style': 'resize:none'})}

        help_texts = {'adv_desc': _('Advertisement Description. HashTag must be written here.'),
                      'adv_min_follower': _('Influencer''s minimum follower count'),
                      'adv_max_follower': _('Influencer''s maximum follower count'),
                      }

    def clean_categories(self):
        data = self.cleaned_data['categories']

        if not data:
            raise forms.ValidationError(_('*Please select at least one category'))
        return data

    def clean_adv_desc(self):
        data = self.cleaned_data['adv_desc']
        rexp = re.compile("(#\w+)")
        hashtags = rexp.findall(data)

        if data.strip() == '' or not data:
            raise forms.ValidationError(_('*Required Field'))
        elif not hashtags:
            raise forms.ValidationError(_('*Please specify hashtags'))
        return data

    def clean_adv_max_follower(self):
        data = self.cleaned_data['adv_max_follower']

        if not data:
            raise forms.ValidationError(_('*Required Field'))
        elif data < 0 or data == 0:
            raise forms.ValidationError(_('*Max follower value must be bigger than 0'))
        return data

    def clean_adv_min_follower(self):
        data = self.cleaned_data['adv_min_follower']

        if not data:
            raise forms.ValidationError(_('*Required Field'))
        elif data < 0 or data == 0:
            raise forms.ValidationError(_('*Min follower value must be bigger than 0'))
        return data
