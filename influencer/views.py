from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.


@login_required
def ad_recommend_list(request):
    return render(request, 'influencer/inf_ad_suggestion.html')
