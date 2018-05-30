from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import AdvertisementSoftForm, AdvertisementDetailForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.serializers.json import DjangoJSONEncoder
import json
from decimal import Decimal


@login_required()
def summary(request):
    if request.method == 'POST':
        create_advertisement_soft_form = AdvertisementSoftForm(request.POST)

        if create_advertisement_soft_form.is_valid():
            request.session['name'] = create_advertisement_soft_form.cleaned_data['name']
            request.session['budget'] = json.dumps(create_advertisement_soft_form.cleaned_data['budget'],
                                                   cls=DjangoJSONEncoder)
            request.session['max_fee_per_like'] = create_advertisement_soft_form.cleaned_data['max_fee_per_like']
            request.session['expire_date'] = json.dumps(create_advertisement_soft_form.cleaned_data['expire_date'],
                                                        cls=DjangoJSONEncoder)

            request.session['is_next'] = True
            # request.session['adv_info'] = json.dumps(form.cleaned_data, cls=DjangoJSONEncoder)

            return HttpResponseRedirect(reverse('advertisement:create_adv'))

    else:
        create_advertisement_soft_form = AdvertisementSoftForm()
    return render(request, 'advertisement/adv_summary.html',
                  {'create_advertisement_soft_form': create_advertisement_soft_form})


@login_required()
def create_adv(request):
    if request.session.get('is_next'):
        if request.method == 'POST':
            pass
        elif request.method == 'GET':
            adv_soft = dict()
            adv_soft['name'] = request.session.get('name')
            adv_soft['budget'] = Decimal(request.session.get('budget').strip('"'))
            adv_soft['max_fee_per_like'] = request.session.get('max_fee_per_like')
            adv_soft['expire_date'] = request.session.get('expire_date')

            create_advertisement_detail_form = AdvertisementDetailForm()

            return render(request, 'advertisement/create_adv.html',
                          {'create_advertisement_detail_form': create_advertisement_detail_form,
                           'adv_soft': adv_soft})
        else:
            return redirect('home')
    else:
        return redirect('create_adv')
