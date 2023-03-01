import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from hello.forms import LogMessageForm, CreateUserForm
from hello.models import LogMessage
from django.views.generic import ListView
from .models import Profile, addListings, userinfo, Shome, allinformation
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage
    #this cant be inside here but theres nowhere else to put it, need new homepage

def home(request):
    shome_list = allinformation.objects.all()
    return render(request, 'hello/home.html', {'shome_list': shome_list})


def allInfoDisplay(request):
    user = request.user
    add = request.POST.get("address")
    cit = request.POST.get("city")
    zip = request.POST.get("zip")
    hometype = request.POST.get("hometype")
    pri = request.POST.get("price")
    dep = request.POST.get("deposit")
    roo = request.POST.get("rooms")
    gen = request.POST.get("gender")
    beds = request.POST.get("beds")
    size = request.POST.get("size")
    bath = request.POST.get("bath")
    renetc = request.POST.get("rent_etc")
    park = request.POST.get("parking")
    inter = request.POST.get("internet")
    pet = request.POST.get("pets")
    ac = request.POST.get("ac")
    heat = request.POST.get("heat")
    lau = request.POST.get("laundry")
    tv = request.POST.get("tv")
    ammetc = request.POST.get("etc")
    image = request.POST.get("img")
    allinformation(user = user, address = add, city = cit, zip = zip,hometype = hometype, beds = beds, size = size, bath = bath, monthlyprice = pri, securitydeposit = dep, numbertenants = roo, gender = gen, addrentinfo = renetc, parking = park, internet = inter, pets = pet, aircond = ac, heating = heat, laundry = lau, streamingservices = tv, addamenityinfo = ammetc, image = image).save()
    return render(request, "hello/home.html", )


def profile(request):
    addyinfo = allinformation.objects.filter(user=request.user).last()
    return render(request, "hello/profile.html", {'addyinfo': addyinfo,})

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
    
    addyinfo = allinformation.objects.filter(user=request.user).last()
        
    return render(request, "hello/listing.html", {'addyinfo': addyinfo,})

def edit_listing(request):
    addyinfo = allinformation.objects.last()
        
    return render(request, "hello/edit_listing.html", {'addyinfo': addyinfo,})


def test(request):
    allInfoDisplay = allinformation.objects.last()
        
    return render(request, "hello/listing.html", {'allInfoDisplay': allInfoDisplay,})




# def display(request):
#     print('test')
#     add = request.POST.get("address")
#     cit = request.POST.get("city")
#     zip = request.POST.get("zip")
#     pri = request.POST.get("price")
#     dep = request.POST.get("deposit")
#     roo = request.POST.get("rooms")
#     gen = request.POST.get("gender")
#     renetc = request.POST.get("rent_etc")
#     park = request.POST.get("parking")
#     inter = request.POST.get("internet")
#     pet = request.POST.get("pets")
#     ac = request.POST.get("ac")
#     heat = request.POST.get("heat")
#     lau = request.POST.get("laundry")
#     tv = request.POST.get("tv")
#     ammetc = request.POST.get("etc")
#     message = add, cit, zip, pri, dep, roo, gen, renetc, park, inter, pet, ac, heat, lau, ammetc
#     # addressinformation(address = add, city = cit, zip = zip).save()
#     # rentinformation(monthlyprice = pri, securitydeposit = dep, numbertenants = roo, addrentinfo = renetc).save()
#     # amenityinfo(parking = park, internet = inter, pets = pet, aircond = ac, heating = heat, laundry = lau, streamingservices = tv, addamenityinfo = ammetc,).save()
#     return render(request, "hello/test.html")
    



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
    

def userdisplay(request):
    form = CreateUserForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            # message = form.save(commit=False)
            first = request.POST.get("firstname")
            last = request.POST.get("lastname")
            uname = request.POST.get("username")
            passw = request.POST.get("password")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            gen = request.POST.get("gender")
            # userinfo(firstname = first, lastname = last, username = uname, password = passw, email = email, phone = phone, gender = gen).save()
            # user = User.objects.create_user(uname, email, passw)
            new_user = form.save(commit=False)
            new_user.save()
            return render(request, "hello/login_home.html")
        else:
            return render(request, "hello/test.html")



# if __name__ == '__main__':
#     all_ammenities() 

def authenticateuser(request):
    form = CreateUserForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            checkusername = request.POST.get("username")
            checkpassword = request.POST.get("password")
        else:
            print("test")
            return render(request, "hello/test.html")
    print(checkusername, checkpassword)
    user = authenticate(username=checkusername, password=checkpassword)
    if user is not None:
       login(request, user) 
       return render(request, "hello/home.html")
    else:
        return render(request, "hello/create_acc.html")


# if userinfo.objects.filter(email=checkemail).exists():
#         userdata = userinfo.objects.filter(email=checkemail).values()[0]
#         print(userdata["password"])
#         if userdata["password"] == checkpassword:
#             return render(request, "hello/home.html")
#         else:
#             return render(request, "hello/create_acc.html")
#     else:
#         return render(request, "hello/test.html")
            
            
            
            
        
 
    
    
    
