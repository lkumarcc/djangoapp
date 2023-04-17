import PIL
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import post_save # Produce a signal if there is any database action.
from PIL import Image, ImageOps

class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"



#info from dwitter
# to couple each profile to exactly one user
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
   # email = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    gender = models.CharField(max_length=30, blank=True, null=True)
   # firstname = models.CharField(max_length=12, blank=True, null=True)
   # lastname = models.CharField(max_length=12, blank=True, null=True)
   # username = models.CharField(max_length=12, blank=True, null=True)
   # password = models.CharField(max_length=12, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(max_length=600, blank=True, null=True)  
    profile_pic = models.ImageField(upload_to="images/profilepics/",default="images/profilepics/default_profile_pic.jpg", height_field=None, width_field=None, max_length=500,blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=22, blank=True, null=True)
    insta = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.user)
    
    """
    This code is causing a bug:

    #resize profile pics 
    def save(self, *args, **kwargs):
        super().save(*args, *kwargs)
        SIZE = (170,170)
        print(self.profile_pic.path)
        if self.profile_pic:
            img = Image.open(self.profile_pic.path)
            img = ImageOps.exif_transpose(img)
            #img = ImageOps.crop()
            img.resize(SIZE, Image.LANCZOS)
            img.save(self.profile_pic.path)
    """
"""   
Code Not needed: 

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
"""

class changePass(models.Model):
    password=models.CharField(max_length=200)
    
class addListings(models.Model):
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    zip = models.IntegerField( blank=True, null=True)
    price = models.DecimalField(max_digits = 100, decimal_places=2, blank=True, null=True)
    rooms = models.IntegerField( blank=True, null=True)
    file = models.FileField

#new class that takes in all of the info for address info, rent info, amenity info, shome
class allinformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    zip = models.IntegerField( blank=True, null=True)
    state = models.CharField(max_length=22, blank=True, null=True)
    hometype = models.CharField(max_length=100, blank=True, null=True)
    monthlyprice = models.DecimalField(max_digits = 100, decimal_places=2, blank=True, null=True)
    securitydeposit = models.DecimalField(max_digits = 100, decimal_places=2, blank=True, null=True)
    numbertenants = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    beds = models.IntegerField( blank=True, null=True)
    #size = models.IntegerField( blank=True, null=True)
    #bath = models.DecimalField(max_digits = 100, decimal_places=1, blank=True, null=True)
    addrentinfo = models.CharField(max_length=300, blank=True, null=True)
    parking = models.CharField(max_length=4, blank=True, null=True)
    #internet = models.CharField(max_length=4, blank=True, null=True)
    pets = models.CharField(max_length=4, blank=True, null=True)
    #aircond = models.CharField(max_length=4, blank=True, null=True)
    #heating = models.CharField(max_length=4, blank=True, null=True)
    laundry = models.CharField(max_length=20, blank=True, null=True)
    #streamingservices = models.CharField(max_length=4, blank=True, null=True)
    addamenityinfo = models.CharField(max_length=300, blank=True, null=True)
    image = models.ImageField(upload_to="images/",default="images/image_coming_soon.png", height_field=None, width_field=None, max_length=100,blank=True, null=True)
    #need to upate forms to account for hometype, size, beds, bath
    
   
'''
class addressinformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    zip = models.IntegerField( blank=True, null=True)
    
    
class rentinformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    monthlyprice = models.DecimalField(max_digits = 100, decimal_places=2, blank=True, null=True)
    securitydeposit = models.DecimalField(max_digits = 100, decimal_places=2, blank=True, null=True)
    numbertenants = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    beds = models.IntegerField(blank=True, null=True)
    addrentinfo = models.CharField(max_length=300, blank=True, null=True)
    
class amenityinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    parking = models.CharField(max_length=4, blank=True, null=True)
    #internet = models.CharField(max_length=4, blank=True, null=True)
    pets = models.CharField(max_length=4, blank=True, null=True)
    #aircond = models.CharField(max_length=4, blank=True, null=True)
    #heating = models.CharField(max_length=4, blank=True, null=True)
    laundry = models.CharField(max_length=20, blank=True, null=True)
    #streamingservices = models.CharField(max_length=4, blank=True, null=True)
    addamenityinfo = models.CharField(max_length=300, blank=True, null=True)
'''    

class Shome(models.Model):
    hometype = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField( blank=True, null=True)
    addy = models.CharField(max_length=100, blank=True, null=True)
    size = models.IntegerField( blank=True, null=True)
    beds = models.IntegerField( blank=True, null=True)
    bath = models.DecimalField(max_digits = 100, decimal_places=1, blank=True, null=True)
    
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing =  models.ForeignKey(allinformation, on_delete=models.CASCADE)
    
