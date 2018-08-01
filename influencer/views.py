from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic
from advertisement.models import AdvSummary
from influencer.models import InfluencerSummary
from django.utils import timezone


@login_required
def ad_recommend_list(request):
    return render(request, 'influencer/inf_ad_suggestion.html')


class InfAdvertisementList(generic.ListView):
    model = AdvSummary
    template_name = 'influencer/inf_ad_suggestion.html'
    context_object_name = 'advertisement_list'

    def get_queryset(self):
        return AdvSummary.filter(expire_date__gte=timezone.now()).filter(publish_date__isnull=False). \
            order_by('-publish_date')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['registered_adv'] = InfluencerSummary.objects.all()
        return context
