from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from advertisement.models import AdvSummary
from django.utils.text import slugify
from .forms import AdvertisementSoftForm
from django.utils import timezone
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

User = get_user_model()


class CreateAdvertisement(generic.CreateView):
    form_class = AdvertisementSoftForm
    template_name = 'brand/advertisement_brand_home.html'
    context_object_name = 'create_advertisement_form'
    model = AdvSummary

    def form_valid(self, form):
        new_adv = form.save(commit=False)
        new_adv.slug_name = slugify(new_adv.name + "_" + str(new_adv.guid))
        new_adv.username = self.request.user
        new_adv.save()
        return super().form_valid(form)


class PublishedAdvertisementList(generic.ListView):
    model = AdvSummary
    paginate_by = 3
    template_name = 'brand/advertisement_brand_home.html'
    context_object_name = 'advertisement_list'

    def get_queryset(self):
        return AdvSummary.objects.filter(username__exact=self.request.user).filter(expire_date__gte=timezone.now()).\
            filter(publish_date__isnull=False).order_by('-publish_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_advertisement_form'] = AdvertisementSoftForm()
        #context['is_paginated'] = True
        unpublished_advertisement_list = AdvSummary.objects.filter(username__exact=self.request.user).\
            filter(expire_date__gte=timezone.now()). \
            filter(publish_date__isnull=True).order_by('create_date')
        # paginator = Paginator(unpublished_advertisement_list, 3)
        # page = self.request.GET.get('page')
        context['unpublished_advertisement_list'] = unpublished_advertisement_list

        context['top5_advertisement_list'] = AdvSummary.objects.filter(expire_date__gte=timezone.now()). \
            filter(publish_date__isnull=False).order_by('adv_stats__number_of_likes')

        return context


class BrandHomePage(LoginRequiredMixin, generic.View):
    login_url = '/'
    redirect_field_name = '/'

    def post(self, request, *args, **kwargs):
        view = CreateAdvertisement.as_view()
        return view(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        view = PublishedAdvertisementList.as_view()
        return view(request, *args, **kwargs)