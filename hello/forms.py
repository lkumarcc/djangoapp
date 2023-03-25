from django import forms
from hello.models import LogMessage
from .models import allinformation, Profile
from django.core.validators import RegexValidator, FileExtensionValidator
from django.db import models
from django.forms import ModelForm, Textarea
#from betterforms.multiform import MultiModelForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user
from django.contrib.auth.forms import UserCreationForm

address_validation = RegexValidator(r'^(\d+) ?([A-Za-z](?= ))? (.*?) ([^ ]+?) ?((?<= )APT)? ?((?<= )\d*)?$', 'Invalid Address. Please enter address as: Street Number Street Prefix (Optional) Street Name Street Suffix Apt/Suite (Optional) Apt Number (Optional)')
letters_only = RegexValidator(r'\D+', 'Invalid. Please enter text only')
numbers_only = RegexValidator(r"^[+-]?((\d+(\.\d+)?)|(\.\d+))$", 'Invalid. Please enter numbers only')
name = RegexValidator(r"[A-Za-z '-]+",'Letters Only')
school_email = RegexValidator(r"[a-zA-Z0-9]+@[a-zA-Z]+.edu", 'Enter school email only (.edu)')
phone_number = RegexValidator(r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$", 'Phone Number Only' )

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)   # NOTE: the trailing comma is required

GENDER_CHOICES= (
('', ''),
('Female','Female'),
('Male','Male'),
('Transgender','Transgender'),
('Non-binary/non-conforming', 'Non-binary/non-conforming'), 
('Preferred Not to Share', 'Prefer not to respond'), 
)

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
('apartment','Apartment'),
('house','House'),
('townhome',"Townhome"),
)

GENDER_LISTING_CHOICES= (
('', ''),
('women only','Women Only'),
('men only','Men Only'),
('all inclusive','All inclusive'),
)
PARKING_CHOICES= (
('', ''),
('yes','Yes'),
('no','No'),
)

PETS_CHOICES= (
('', ''),
('yes','Yes'),
('no','No'),
)

LAUNDRY_CHOICES= (
('', ''),
('in unit','In Unit'),
('out of unit','Out of Unit'),
('no','No'),
)

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs = {'class':'form-control','title':'Example@University.edu'}), validators=[school_email], required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control','title':'First Name', 'max_length':50}), required=True, validators=[name])
    last_name = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control','max_length':50, 'title': 'Last Name'}), required=True)
    username = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control','max_length':50}), required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs = {'class':'form-control','max_length':50}), label="Password", required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs = {'class':'form-control','max_length':50}), label="Confirm Password", required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control','title':'1234567891', 'maxLength': 10}), validators=[phone_number])
    school = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control','title': 'Ex. Tulane University', 'maxLength': 100}), required=True, validators=[letters_only])
    gender = forms.CharField(widget=forms.Select(attrs ={'class':'form-select'}, choices=GENDER_CHOICES),required =True)

    class Meta:
        model = User
        fields = ("username","first_name", "last_name", "email", "password1", "password2", "phone", "school", "gender")
    #might implement for password - using standard validation now but has more features 
    #pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}"
    #<p style="color:red;"><small>Password must contain at least one number, one uppercase character, one lowercase character, and at least 8 characters</small></p>


class EditProfileForm(ModelForm):
   # firstname = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control', 'title':'First Name', 'maxLength': 12}), required=True, validators=[name])
   # lastname = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control', 'maxLength': 12}), required=True, validators=[name])
   # username = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control', 'maxLength': 12}), required=True, validators=[name])  
   # email = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control','title': 'School Email Only (.edu)', 'maxLength': 30}), required=True, validators=[school_email])
    phone = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control','title':'1234567891', 'maxLength': 10}),required=False, validators=[phone_number])
    school = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control','title': 'Ex. Tulane University', 'maxLength': 30}), required=True, validators=[letters_only])
    gender = forms.CharField(widget=forms.Select(attrs ={'class':'form-select'}, choices=GENDER_CHOICES),required =True)
    bio = forms.CharField(widget=forms.Textarea(attrs = {'class':'form-control', 'title':'Bio', 'maxLength': 600}), required=False)
    profile_pic = forms.ImageField(label="Profile Picture", validators=[FileExtensionValidator(['jpg', 'jpeg'])])
    city = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control','title': 'City', 'maxLength': 30}), required=False, validators=[letters_only])
    state = forms.CharField(widget=forms.Select(attrs ={'class':'form-select'}, choices=STATE_CHOICES), required=False)
    insta = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control','title': 'Ex: https://www.instagram.com/tulaneu/', 'maxLength': 50}),required=False, validators=[letters_only])

    class Meta: 
        model = Profile
        #match database fields 
        fields = ("phone", "school", "gender", "city", "state", "insta", "bio", "profile_pic")
        exclude = ['user']

class AddListingForm(ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control', 'title':'Example: 123456 Street Name', 'maxLength': 75}), required=True, validators=[address_validation])
    city = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control', 'maxLength': 30}), required=True, validators=[letters_only])
    zip = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control','title': 'Example: 12345', 'maxLength': 5}), required=True, validators=[numbers_only])
    state = forms.CharField(widget=forms.Select(attrs ={'class':'form-select'}, choices=STATE_CHOICES),required =True)
    hometype = forms.CharField(widget=forms.Select(attrs ={'class':'form-select'}, choices=HOMETYPE_CHOICES),required =True, label="Home Type")
    monthlyprice = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control','title': 'Example: 450', 'maxLength': 5}), required=True, validators=[numbers_only], label="Monthly Lease Price")
    securitydeposit = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control','title': 'Example: 700', 'maxLength': 5}), required=True, validators=[numbers_only], label="Security Deposit")
    numbertenants = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control','title': 'Example: 4', 'maxLength': 2}), required=True, validators=[numbers_only], label="Total Number of Tenants")
    gender = forms.CharField(widget=forms.Select(attrs ={'class':'form-select'}, choices=GENDER_LISTING_CHOICES),required =True)
    beds = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control','title': 'Example: 4', 'maxLength': 2}), required=True, validators=[numbers_only], label="Bedrooms Available")
    addrentinfo = forms.CharField(widget=forms.Textarea(attrs = {'class':'form-control','title': 'Utilities not included in rent, upper property in duplex, two entrances to apartment, etc.', 'maxLength': 255}), label="Additional Information", required=False)
    parking = forms.CharField(widget=forms.Select(attrs ={'class':'form-select'}, choices=PARKING_CHOICES),required =True)
    pets = forms.CharField(widget=forms.Select(attrs ={'class':'form-select'}, choices=PETS_CHOICES),required =True)
    laundry = forms.CharField(widget=forms.Select(attrs ={'class':'form-select'}, choices=LAUNDRY_CHOICES),required =True)
    addamenityinfo = forms.CharField(widget=forms.Textarea(attrs = {'class':'form-control','title': 'Backyard pool, large front porch, fireplace in living room, etc.', 'maxLength': 255}), label="Additional Amenities", required=False)
    image = forms.ImageField(label="Listing Main Image", required=False, validators=[FileExtensionValidator(['jpg', 'jpeg'])])
   
    #belongs inside each form class
    class Meta: 
        model = allinformation
        #match database fields 
        fields = ( "address", "city", "zip", "state","hometype", "monthlyprice", "securitydeposit", "numbertenants", "gender", "beds", "addrentinfo", "parking", "pets", "laundry", "addamenityinfo","image")
        exclude = ['user']

        
class DeleteFavorites(forms.Form):
    listing_id = forms.CharField(label='listing_id', max_length=100)