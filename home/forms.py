from collections import Iterable
import datetime

from django.forms import ModelForm, CharField, ModelChoiceField, ModelMultipleChoiceField
from django.forms.fields import ChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from models import Section, Donation, PMT_CHOICES

AMOUNT_CHOICES = (
    ('', ''),
    (20, '$20'),
    (10, '$10'),
    (5, '$5'),
)

PC_CHOICES = (
    ('', ''),
    (True, 'definitely want'),
    (False, "don't really need"),
)

MO_CHOICES = (
    ('01', 'January'),
    ('02', 'February'),
    ('03', 'March'),
    ('04', 'April'),
    ('05', 'May'),
    ('06', 'June'),
    ('07', 'July'),
    ('08', 'August'),
    ('09', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December'),
)

YR_CHOICES = []
for x in range(8):
    yr = datetime.date.today().year + x
    YR_CHOICES.append((yr, yr))
YR_CHOICES = tuple(YR_CHOICES)

class DonationForm(ModelForm):
    month = ChoiceField(choices=MO_CHOICES)
    year = ChoiceField(choices=YR_CHOICES)
    postcard = ChoiceField(choices=PC_CHOICES)
    amount = ChoiceField(choices=AMOUNT_CHOICES)
    payment_type = ChoiceField(choices=PMT_CHOICES)
    zip = CharField(max_length=5, required=False)
    sections = ModelChoiceField(required=True, empty_label='',
        queryset=Section.objects.all()
    )
    class Meta:
        model = Donation
        exclude = ['date', 'received', 'cleared', ]

    def clean(self):
        cleaned_data = super(DonationForm, self).clean()

        # fix postcard value
        if cleaned_data['postcard'] == 'True':
            cleaned_data['postcard'] = True
        else:
            cleaned_data['postcard'] = False

        # make sure sections is a list
        if not isinstance(cleaned_data['sections'], Iterable):
            cleaned_data['sections'] = [cleaned_data['sections'],]

        # if postcard, make sure address is good
        if cleaned_data['postcard']:
            if not cleaned_data['address'] or not cleaned_data['city'] or not cleaned_data['state'] or not cleaned_data['zip']:
                self.errors['address'] = "I know you want a postcard, but you've to tell me where to send it!"

        return cleaned_data
