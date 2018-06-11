from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import generic
from .models import AdvSummary
from django.utils.text import slugify

from .forms import AdvertisementSoftForm, AdvertisementDetailForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.serializers.json import DjangoJSONEncoder
import json
from decimal import Decimal


class CreateAdvertisement(LoginRequiredMixin, generic.CreateView):
    form_class = AdvertisementSoftForm
    template_name = 'advertisement/create_advertisement.html'

    def get_context_data(self, **kwargs):
        context = super(CreateAdvertisement, self).get_context_data()
        context['create_advertisement_form'] = context['form']
        return context

    def form_valid(self, form):
        new_adv = form.save(commit=False)
        new_adv.adv_slug_name = slugify(new_adv.name)
        new_adv.username = self.request.user
        new_adv.save()
        return super().form_valid(form)


class PublishAdvertisementDisplay(generic.DetailView):
    model = AdvSummary
    template_name = 'advertisement/publish_advertisement.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AdvertisementDetailForm()
        return context


class PublishAdvertisementForm(generic.detail.SingleObjectMixin, generic.FormView):
    template_name = 'advertisement/publish_advertisement.html'
    form_class = AdvertisementDetailForm
    model = AdvSummary

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('adv-detail', kwargs={'pk': self.object.pk})


class PublishAdvertisement(generic.View):
    def get(self, request, *args, **kwargs):
        view = PublishAdvertisementDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PublishAdvertisementForm.as_view()
        return view(request, *args, **kwargs)

# @login_required()
# def summary(request):
#     if request.method == 'POST':
#         create_advertisement_soft_form = AdvertisementSoftForm(request.POST)
#
#         if create_advertisement_soft_form.is_valid():
#             request.session['name'] = create_advertisement_soft_form.cleaned_data['name']
#             request.session['budget'] = json.dumps(create_advertisement_soft_form.cleaned_data['budget'],
#                                                    cls=DjangoJSONEncoder)
#             request.session['max_fee_per_like'] = create_advertisement_soft_form.cleaned_data['max_fee_per_like']
#             request.session['expire_date'] = json.dumps(create_advertisement_soft_form.cleaned_data['expire_date'],
#                                                         cls=DjangoJSONEncoder)
#
#             request.session['is_next'] = True
#             # request.session['adv_info'] = json.dumps(form.cleaned_data, cls=DjangoJSONEncoder)
#
#             return HttpResponseRedirect(reverse('advertisement:create_adv'))
#
#     else:
#         create_advertisement_soft_form = AdvertisementSoftForm()
#     return render(request, 'advertisement/_adv_summary.html',
#                   {'create_advertisement_soft_form': create_advertisement_soft_form})
#
#
# @login_required()
# def create_adv(request):
#     if request.session.get('is_next'):
#         if request.method == 'POST':
#             pass
#         elif request.method == 'GET':
#             adv_soft = dict()
#             adv_soft['name'] = request.session.get('name')
#             adv_soft['budget'] = Decimal(request.session.get('budget').strip('"'))
#             adv_soft['max_fee_per_like'] = request.session.get('max_fee_per_like')
#             adv_soft['expire_date'] = request.session.get('expire_date')
#
#             create_advertisement_detail_form = AdvertisementDetailForm()
#
#             return render(request, 'advertisement/_create_adv.html',
#                           {'create_advertisement_detail_form': create_advertisement_detail_form,
#                            'adv_soft': adv_soft})
#         else:
#             return redirect('home')
#     else:
#         return redirect('create_adv')
