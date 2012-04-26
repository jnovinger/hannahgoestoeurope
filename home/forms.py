from django.forms import ModelForm, CharField, ModelMultipleChoiceField
from django.forms.fields import ChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from models import Section, Donation, PMT_CHOICES

class DonationForm(ModelForm):
    payment_type = ChoiceField(widget=RadioSelect, choices=PMT_CHOICES)
    zip = CharField(max_length=5)
    sections = ModelMultipleChoiceField(required=True,
        widget=CheckboxSelectMultiple,
        queryset=Section.objects.all()
    )
    class Meta:
        model = Donation
        exclude = ['date', 'received', 'cleared', ]