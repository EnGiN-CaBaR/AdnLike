from django.shortcuts import render
from .forms import AdvertisementForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def summary(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            budget = form.cleaned_data['budget']
            max_fee_per_like = form.cleaned_data['max_fee_per_like']
            expire_date = form.cleaned_data['expire_date']

            return HttpResponseRedirect(reverse())

    else:
        createNewAdvertisementForm = AdvertisementForm()

    return render(request, 'adv_details.html', {'createNewAdvertisementForm': createNewAdvertisementForm})
