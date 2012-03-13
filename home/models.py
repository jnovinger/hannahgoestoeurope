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

AMOUNT_CHOICES = (
    (5, '$5'),
    (10, '$10'),
    (999.99, '$1000')

)

class Donation(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=255, blank=True, null=True)

    amount = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    received = models.BooleanField()
    cleared = models.BooleanField()

    def display_name(self):
        return "%s %s." % (self.first_name, self.last_name[:1])

    def __unicode__(self):
        full_name = self.first_name
        full_name = full_name + " " + self.last_name if self.last_name else full_name
        return "%s - $%s" % (full_name, self.amount)

    class Meta:
        ordering = ['date', 'last_name', 'first_name', 'amount', ]