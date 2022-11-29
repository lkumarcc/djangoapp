import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from hello.forms import LogMessageForm
from hello.models import LogMessage
from django.views.generic import ListView
from .models import Profile, addListings, addressinformation, rentinformation, amenityinfo

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def profile(request):
    return render(request, "hello/profile.html")

def messages(request):
    return render(request, "hello/messages.html")

def favorites(request):
    return render(request, "hello/favorites.html")

def add_listing(request):
    return render(request, "hello/add_listing.html")

def about(request):
    return render(request, "hello/about.html")

def create_acc(request):
    return render(request, "hello/create_acc.html")

def login_home(request):
    return render(request, "hello/login_home.html")
    
def listing(request):
    ammenities_list = amenityinfo.objects.last()
    rent_list = rentinformation.objects.last()
    return render(request, "hello/listing.html", {'ammenities_list': ammenities_list,  'rent_list': rent_list})

def test(request):
    ammenities_list = amenityinfo.objects.last()
    rent_list = rentinformation.objects.last()
    return render(request, "hello/test.html", {'ammenities_list': ammenities_list,  'rent_list': rent_list})

def display(request):
    print('test')
    add = request.POST.get("address")
    cit = request.POST.get("city")
    zip = request.POST.get("zip")
    pri = request.POST.get("price")
    dep = request.POST.get("deposit")
    roo = request.POST.get("rooms")
    gen = request.POST.get("gender")
    renetc = request.POST.get("rent_etc")
    park = request.POST.get("parking")
    inter = request.POST.get("internet")
    pet = request.POST.get("pets")
    ac = request.POST.get("ac")
    heat = request.POST.get("heat")
    lau = request.POST.get("laundry")
    tv = request.POST.get("tv")
    ammetc = request.POST.get("etc")
    message = add, cit, zip, pri, dep, roo, gen, renetc, park, inter, pet, ac, heat, lau, ammetc
    addressinformation(address = add, city = cit, zip = zip).save()
    rentinformation(monthlyprice = pri, securitydeposit = dep, numbertenants = roo, addrentinfo = renetc).save()
    amenityinfo(parking = park, internet = inter, pets = pet, aircond = ac, heating = heat, laundry = lau, streamingservices = tv, addamenityinfo = ammetc,).save()
    return render(request, "hello/test.html")
    

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
        
    )

print("http://127.0.0.1:8000/hello/name")

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "hello/log_message.html", {"form": form}) 
    



# if __name__ == '__main__':
#     all_ammenities()