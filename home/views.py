from django.conf import settings
from django.contrib.auth.models import Message
from django.db.models import Sum
from django.shortcuts import render_to_response
from django.template import RequestContext
import stripe

from models import Post, Donation, Section
from forms import DonationForm


def _charge_card(post):
    stripe.api_key = settings.STRIPE_PRIVATE_KEY
    charge = stripe.Charge.create(
        amount=int(float(post['amount']) * 100),
        currency='usd',
        card=post['stripeToken'],
        description="Donation at http://hannahgoestoeurope.com"
    )
    return charge['paid']

def home(request):
    context = {}
    if request.POST:
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)

            if 'stripeToken' in request.POST:
                charged = _charge_card(request.POST)
                if charged:
                    donation.cleared = donation.received = True
            donation.save()
            for sec in form.cleaned_data['sections']:
                donation.sections.add(sec)
            context['thanks'] = form.cleaned_data['first_name']
            context['postcard'] = form.cleaned_data['postcard']

        else:
            context['show_form'] = True
    form = DonationForm

    sections = Section.objects.select_related()
    section_sponsors = {}
    for section in sections:
        section_sponsors[section.slug] = section.donations.all()

    context['sections'] = sections
    context['section_sponsors'] = section_sponsors
    context['form'] = form
    context['stripe_publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY

    return render_to_response('index.html', context, context_instance=RequestContext(request))