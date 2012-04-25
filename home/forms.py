from django.forms import ModelForm, CharField
from django.forms.fields import ChoiceField
from django.forms.widgets import RadioSelect
from models import Donation, PMT_CHOICES

class DonationForm(ModelForm):
    payment_type = ChoiceField(widget=RadioSelect, choices=PMT_CHOICES)
    zip = CharField(max_length=5)
    class Meta:
        model = Donation
        exclude = ['date', 'received', 'cleared', ]