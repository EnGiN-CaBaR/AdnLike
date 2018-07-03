from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views import generic
from .models import AdvSummary, Category
from django.utils.text import slugify

from .forms import AdvertisementSoftForm, AdvertisementDetailForm
from django.urls import reverse_lazy
from django.utils import timezone

User = get_user_model()


class CreateAdvertisement(generic.CreateView):
    form_class = AdvertisementSoftForm
    template_name = 'advertisement/advertisement_brand_home.html'
    context_object_name = 'create_advertisement_form'
    model = AdvSummary

    def form_valid(self, form):
        new_adv = form.save(commit=False)
        new_adv.adv_slug_name = slugify(new_adv.name + "_" + str(new_adv.guid))
        new_adv.username = self.request.user
        new_adv.save()
        return super().form_valid(form)


class PublishedAdvertisementList(generic.ListView):
    model = AdvSummary
    paginate_by = 5
    template_name = 'advertisement/advertisement_brand_home.html'
    context_object_name = 'advertisement_list'

    def get_queryset(self):
        query_set1 = AdvSummary.objects.filter(username__exact=self.request.user).filter(expire_date__gte=timezone.now()).\
            filter(publish_date__isnull=False).order_by('-publish_date')
        query_set2 = AdvSummary.objects.filter(expire_date__gte=timezone.now()). \
            filter(publish_date__isnull=False).order_by('-')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_advertisement_form'] = AdvertisementSoftForm()
        return context


class BrandAdvertisementCreatePublishPage(LoginRequiredMixin, generic.View):
    login_url = '/'
    redirect_field_name = '/'

    def post(self, request, *args, **kwargs):
        view = CreateAdvertisement.as_view()
        return view(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        view = PublishedAdvertisementList.as_view()
        return view(request, *args, **kwargs)


class PublishAdvertisementDetail(generic.DetailView):
    model = AdvSummary
    template_name = 'advertisement/publish_advertisement.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AdvertisementDetailForm()
        return context


class PublishAdvertisementCreate(generic.detail.SingleObjectMixin, generic.FormView):
    template_name = 'advertisement/publish_advertisement.html'
    form_class = AdvertisementDetailForm
    model = AdvSummary

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('advertisement:create')

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(AdvSummary, pk=pk)
        obj.advertisement_image = form.cleaned_data['advertisement_image']
        obj.adv_max_follower = self.request.POST['adv_max_follower']
        obj.adv_min_follower = self.request.POST['adv_min_follower']
        obj.adv_desc = self.request.POST['adv_desc']
        selected_categories = Category.objects.filter(pk__in=self.request.POST.getlist('categories'))
        obj.categories.add(*[cat for cat in selected_categories])
        obj.publish_date = timezone.now()
        obj.save()
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


class UpdateAdvertisement(LoginRequiredMixin, generic.UpdateView):
    form_class = AdvertisementSoftForm
    template_name = 'advertisement/update_advertisement.html'

    form_class = AdvertisementSoftForm

    model = AdvSummary













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
