from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.profile.id])
        user_profile.save()

# Create a Profile for each new user.
#post_save.connect(create_profile, sender=User)

#info from dwitter
# to couple each profile to exactly one user
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
    
    
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
    hometype = models.CharField(max_length=100, blank=True, null=True)
    monthlyprice = models.DecimalField(max_digits = 100, decimal_places=2, blank=True, null=True)
    securitydeposit = models.DecimalField(max_digits = 100, decimal_places=2, blank=True, null=True)
    numbertenants = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    beds = models.IntegerField( blank=True, null=True)
    size = models.IntegerField( blank=True, null=True)
    bath = models.DecimalField(max_digits = 100, decimal_places=1, blank=True, null=True)
    addrentinfo = models.CharField(max_length=300, blank=True, null=True)
    parking = models.CharField(max_length=4, blank=True, null=True)
    internet = models.CharField(max_length=4, blank=True, null=True)
    pets = models.CharField(max_length=4, blank=True, null=True)
    aircond = models.CharField(max_length=4, blank=True, null=True)
    heating = models.CharField(max_length=4, blank=True, null=True)
    laundry = models.CharField(max_length=20, blank=True, null=True)
    streamingservices = models.CharField(max_length=4, blank=True, null=True)
    addamenityinfo = models.CharField(max_length=300, blank=True, null=True)
    images = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,blank=True, null=True )
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
    addrentinfo = models.CharField(max_length=300, blank=True, null=True)
    
class amenityinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    parking = models.CharField(max_length=4, blank=True, null=True)
    internet = models.CharField(max_length=4, blank=True, null=True)
    pets = models.CharField(max_length=4, blank=True, null=True)
    aircond = models.CharField(max_length=4, blank=True, null=True)
    heating = models.CharField(max_length=4, blank=True, null=True)
    laundry = models.CharField(max_length=20, blank=True, null=True)
    streamingservices = models.CharField(max_length=4, blank=True, null=True)
    addamenityinfo = models.CharField(max_length=300, blank=True, null=True)
'''

class userinfo(models.Model):
    email = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    gender = models.CharField(max_length=12, blank=True, null=True)
    firstname = models.CharField(max_length=12, blank=True, null=True)
    lastname = models.CharField(max_length=12, blank=True, null=True)
    username = models.CharField(max_length=12, blank=True, null=True)
    password = models.CharField(max_length=12, blank=True, null=True)
    # models.IntegerField(blank=True, null=True)
class Shome(models.Model):
    hometype = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField( blank=True, null=True)
    addy = models.CharField(max_length=100, blank=True, null=True)
    size = models.IntegerField( blank=True, null=True)
    beds = models.IntegerField( blank=True, null=True)
    bath = models.DecimalField(max_digits = 100, decimal_places=1, blank=True, null=True)
    
#test 