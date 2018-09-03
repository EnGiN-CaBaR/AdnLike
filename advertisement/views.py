from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views import generic
from django.forms import formset_factory
from advertisement.forms import AdvertisementImageForm
from .models import AdvSummary, Category

from .forms import AdvertisementDetailForm
from django.urls import reverse_lazy
from django.utils import timezone

User = get_user_model()


class PublishAdvertisementDetail(generic.DetailView):
    model = AdvSummary
    template_name = 'advertisement/publish_advertisement.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AdvertisementDetailForm()
        context['formset_image'] = formset_factory(AdvertisementImageForm)
        return context


class PublishAdvertisementCreate(generic.UpdateView):
    template_name = 'advertisement/publish_advertisement.html'
    form_class = AdvertisementDetailForm
    model = AdvSummary

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.advertisement_image = form.cleaned_data['advertisement_image']
        obj.adv_max_follower = self.request.POST['adv_max_follower']
        obj.adv_min_follower = self.request.POST['adv_min_follower']
        obj.adv_desc = self.request.POST['adv_desc']
        selected_categories = Category.objects.filter(pk__in=self.request.POST.getlist('categories'))
        obj.categories.add(*[cat for cat in selected_categories])
        obj.publish_date = timezone.now()
        return super().form_valid(form)


class PublishAdvertisement(LoginRequiredMixin, generic.View):
    login_url = '/'
    redirect_field_name = '/'

    def get(self, request, *args, **kwargs):
        view = PublishAdvertisementDetail.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PublishAdvertisementCreate.as_view()
        return view(request, *args, **kwargs)


class DeleteAdvertisement(generic.DeleteView):
    model = AdvSummary
    success_url = reverse_lazy('brand:brand_home')
    template_name = 'advertisement/delete_advertisement.html'


class AdvertisementDetail(LoginRequiredMixin, generic.DetailView):
    login_url = '/'
    redirect_field_name = '/'


