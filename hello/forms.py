from django import forms
from hello.models import LogMessage
from hello.models import userinfo
from .models import allinformation
from django.core.validators import RegexValidator, FileExtensionValidator
from django.db import models
from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User
from django.contrib.auth import get_user

address_validation = RegexValidator(r'^(\d+) ?([A-Za-z](?= ))? (.*?) ([^ ]+?) ?((?<= )APT)? ?((?<= )\d*)?$', 'Invalid Address. Please enter address as: Street Number Street Prefix (Optional) Street Name Street Suffix Apt/Suite (Optional) Apt Number (Optional)')
letters_only = RegexValidator(r'\D+', 'Invalid. Please enter text only')
numbers_only = RegexValidator(r'^[0-9]+$', 'Invalid. Please enter numbers only')


class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)   # NOTE: the trailing comma is required

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = userinfo
        fields = ("email", "phone", "gender", "firstname", "lastname", "username","password", "school",) 

STATE_CHOICES= (
        ('',''),
        ('AL','Alabama'),
        ('AK','Alaska'),
        ('AS','American Samoa'),
        ('AZ','Arizona'),
        ('AR','Arkansas'),
        ('CA','California'),
        ('CO','Colorado'),
        ('CT','Connecticut'),
        ('DE','Delaware'),
        ('DC','District of Columbia'),
        ('FL','Florida'),
        ('GA','Georgia'),
        ('GU','Guam'),
        ('HI','Hawaii'),
        ('ID','Idaho'),
        ('IL','Illinois'),
        ('IN','Indiana'),
        ('IA','Iowa'),
        ('KS','Kansas'),
        ('KY','Kentucky'),
        ('LA','Louisiana'),
        ('ME','Maine'),
        ('MD','Maryland'),
        ('MA','Massachusetts'),
        ('MI','Michigan'),
        ('MN','Minnesota'),
        ('MS','Mississippi'),
        ('MO','Missouri'),
        ('MT','Montana'),
        ('NE','Nebraska'),
        ('NV','Nevada'),
        ('NH','New Hampshire'),
        ('NJ','New Jersey'),
        ('NM','New Mexico'),
        ('NY','New York'),
        ('NC','North Carolina'),
        ('ND','North Dakota'),
        ('MP','Northern Mariana Islands'),
        ('OH','Ohio'),
        ('OK','Oklahoma'),
        ('OR','Oregon'),
        ('PA','Pennsylvania'),
        ('PR','Puerto Rico'),
        ('RI','Rhode Island'),
        ('SC','South Carolina'),
        ('SD','South Dakota'),
        ('TN','Tennessee'),
        ('TX','Texas'),
        ('UT','Utah'),
        ('VT','Vermont'),
        ('VI','Virgin Islands'),
        ('VA','Virginia'),
        ('WA','Washington'),
        ('WV','West Virginia'),
        ('WI','Wisconsin'),
        ('WY','Wyoming')
)

HOMETYPE_CHOICES= (
('', ''),
('Apartment','Apartment'),
('House','House'),
('Townhome',"Townhome"),
)

GENDER_CHOICES= (
('', ''),
('Women Only','Women Only'),
('Men Only','Men Only'),
('All Inclusive','All inclusive'),
)
PARKING_CHOICES= (
('', ''),
('Yes','Yes'),
('No','No'),
)

PETS_CHOICES= (
('', ''),
('Yes','Yes'),
('No','No'),
)

LAUNDRY_CHOICES= (
('', ''),
('In Unit','In Unit'),
('Out Of Unit','Out of Unit'),
('No','No'),
)
class AddListingForm(ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control', 'title':'Example: 123456 Street Name', 'maxLength': 75}), required=True, validators=[address_validation])
    city = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control', 'maxLength': 30}), required=True, validators=[letters_only])
    zip = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control','title': 'Example: 12345', 'maxLength': 5}), required=True, validators=[numbers_only])
    state = forms.CharField(widget=forms.Select(attrs ={'class':'form-select'}, choices=STATE_CHOICES),required =True)
    hometype = forms.CharField(widget=forms.Select(attrs ={'class':'form-select'}, choices=HOMETYPE_CHOICES),required =True, label="Home Type")
    monthlyprice = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control','title': 'Example: 450', 'maxLength': 4}), required=True, validators=[numbers_only], label="Monthly Lease Price")
    securitydeposit = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control','title': 'Example: 700', 'maxLength': 4}), required=True, validators=[numbers_only], label="Estimated Monthly Utilites")
    numbertenants = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control','title': 'Example: 4', 'maxLength': 2}), required=True, validators=[numbers_only], label="Total Number of Tenants")
    gender = forms.CharField(widget=forms.Select(attrs ={'class':'form-select'}, choices=GENDER_CHOICES),required =True)
    beds = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control','title': 'Example: 4', 'maxLength': 2}), required=True, validators=[numbers_only], label="Bedrooms Available")
    addrentinfo = forms.CharField(widget=forms.Textarea(attrs = {'class':'form-control','title': 'Utilities not included in rent, upper property in duplex, two entrances to apartment, etc.', 'maxLength': 300}), label="Additional Information", required=False)
    parking = forms.CharField(widget=forms.Select(attrs ={'class':'form-select'}, choices=PARKING_CHOICES),required =True)
    pets = forms.CharField(widget=forms.Select(attrs ={'class':'form-select'}, choices=PETS_CHOICES),label="Pet Friendly", required =True)
    laundry = forms.CharField(widget=forms.Select(attrs ={'class':'form-select'}, choices=LAUNDRY_CHOICES),required =True)
    addamenityinfo = forms.CharField(widget=forms.Textarea(attrs = {'class':'form-control','title': 'Backyard pool, large front porch, fireplace in living room, etc.', 'maxLength': 300}), label="Additional Amenities", required=False)
    image = forms.ImageField(label="Listing Main Image", required=False, validators=[FileExtensionValidator(['jpg'])])


    class Meta: 
        model = allinformation
        #match database fields 
        fields = ( "address", "city", "zip", "state","hometype", "monthlyprice", "securitydeposit", "numbertenants", "gender", "beds", "addrentinfo", "parking", "pets", "laundry", "addamenityinfo","image")
        exclude = ['user']