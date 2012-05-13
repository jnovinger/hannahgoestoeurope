from math import floor

from django.conf import settings
from django.db.models import Sum
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Post, Donation, Section
from forms import DonationForm

def home(request):
    if request.POST:
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            form = DonationForm
            # don't forget to create success msg
    else:
        form = DonationForm

    posts = Post.objects.filter(is_published=True)[:5]
    sections = Section.objects.all()
    section_sponsors = {}
    for section in sections:
        section_sponsors[section.slug] = section.donations.all()

    return render_to_response(
        'index.html',
        {
            'posts': posts,
            'section_sponsors': section_sponsors,
            'form': form,
            'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
        },
        context_instance=RequestContext(request))
