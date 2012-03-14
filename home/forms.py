from django.forms import ModelForm
from models import Donation

class DonationForm(ModelForm):
    class Meta:
        model = Donation
        exclude = ['date', 'received', 'cleared', ]