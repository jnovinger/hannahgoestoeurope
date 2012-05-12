from django.contrib.localflavor.us.us_states import US_STATES
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    is_published = models.BooleanField()
    publish_date = models.DateField()

    def __unicode__(self):
        return self.title[:50] if len(self.title) > 50 else self.title

    class Meta:
        ordering = ['publish_date', ]

PMT_CHOICES = (
    ('', ''),
    ('check', 'a check'),
    ('cc', 'my credit card'),
)

class Section(models.Model):
    slug = models.SlugField(max_length=6)

    @property
    def title(self):
        return self.slug.title()

    def __unicode__(self):
        return u"%s" % self.title

class Donation(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    card_name = models.CharField(max_length=255, blank=True, null=True, help_text="Your name as it appears on your credit card, if different from above.")

    postcard = models.BooleanField()
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=60, blank=True, null=True)
    state = models.CharField(max_length=2, choices=US_STATES, blank=True, null=True)
    zip = models.CharField(max_length=5, blank=True, null=True)

    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_type = models.CharField(max_length=5, choices=PMT_CHOICES)
    date = models.DateField(auto_now_add=True)

    sections = models.ManyToManyField(Section, related_name='donations')
    received = models.BooleanField()
    cleared = models.BooleanField()

    @property
    def display_name(self):
        return "%s %s." % (self.first_name, self.last_name[:1])

    def __unicode__(self):
        full_name = self.first_name
        full_name = full_name + " " + self.last_name if self.last_name else full_name
        return u"%s - $%s" % (full_name, self.amount)

    class Meta:
        ordering = ['date', 'last_name', 'first_name', 'amount', ]
