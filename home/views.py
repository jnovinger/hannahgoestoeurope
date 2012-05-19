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
    show_form = False
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

            form = DonationForm
            # don't forget to create success msg
        else:
            show_form = True
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
            'show_form': show_form,
            'sections': sections,
            'posts': posts,
            'section_sponsors': section_sponsors,
            'form': form,
            'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
        },
        context_instance=RequestContext(request))
