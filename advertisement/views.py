from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AdvertisementForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import AdvSummary
from django.core.serializers.json import DjangoJSONEncoder
import json
from decimal import Decimal


@login_required()
def summary(request):
    if request.method == 'POST':
        createNewAdvertisementForm = AdvertisementForm(request.POST)

        if createNewAdvertisementForm.is_valid():
            request.session['name'] = createNewAdvertisementForm.cleaned_data['name']
            request.session['budget'] = json.dumps(createNewAdvertisementForm.cleaned_data['budget'], cls=DjangoJSONEncoder)
            request.session['max_fee_per_like'] = createNewAdvertisementForm.cleaned_data['max_fee_per_like']
            request.session['expire_date'] = json.dumps(createNewAdvertisementForm.cleaned_data['expire_date'], cls=DjangoJSONEncoder)

            # request.session['adv_info'] = json.dumps(form.cleaned_data, cls=DjangoJSONEncoder)

            return HttpResponseRedirect(reverse('advertisement:create_adv'))

    else:
        createNewAdvertisementForm = AdvertisementForm()
    return render(request, 'advertisement/adv_summary.html', {'createNewAdvertisementForm': createNewAdvertisementForm})


def create_adv(request):
    if request.method == 'POST':
        request.session.get('name')
        return redirect('home')
    else:
        name = request.session.get('name')
        budget = Decimal(request.session.get('budget').strip('"'))

        return redirect('home')