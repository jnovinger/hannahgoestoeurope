from math import floor

from django.db.models import Sum
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Post, Donation
from forms import DonationForm

def home(request):
    if request.POST:
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DonationForm

    posts = Post.objects.filter(is_published=True)[:5]
    donations = Donation.objects.all()
    donated_amount = donations.aggregate(Sum('amount'))['amount__sum']
    hours = int(floor(donated_amount / 10))
    return render_to_response('index.html',
        {'posts': posts, 'donations': donations, 'form': form, 'donated_amount': donated_amount, 'hours': hours},
        context_instance=RequestContext(request))
