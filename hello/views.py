import re
from django.utils.timezone import datetime
from django.http import HttpResponse, QueryDict
from django.shortcuts import render
from django.shortcuts import redirect
from hello.forms import LogMessageForm, CreateUserForm
from hello.models import LogMessage
from django.views.generic import ListView
from .models import Profile, addListings, userinfo, Shome, allinformation, Favorite
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import AddListingForm
from django.http import HttpResponseRedirect
from decimal import Decimal

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage
    #this cant be inside here but theres nowhere else to put it, need new homepage

def home(request):
    shome_list = allinformation.objects.all()
    print((shome_list))
    return render(request, 'hello/home.html', {'shome_list': shome_list})


def add_listing(request):
    submitted = False
    if request.method =='POST':
        form = AddListingForm(data =request.POST, files = request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.user = request.user
            listing.save()
            return HttpResponseRedirect('/add_listing?submitted=True')
        
    else:
        form = AddListingForm()
        if 'submitted' in request.GET: 
            submitted = True
    return render(request, "hello/add_listing.html", {'form': form, 'submitted': submitted} )

def profile(request):
    addyinfo = allinformation.objects.filter(user=request.user).last()
    return render(request, "hello/profile.html", {'addyinfo': addyinfo,} )

def messages(request):
    return render(request, "hello/messages.html")

def favorites(request):
    listingid = list(Favorite.objects.filter(user=request.user).values("listing_id"))
    print("test3")
    print(listingid)
    listingnums = []
    
    for item in listingid:
        listingnums.append(item["listing_id"])

    addyinfo = allinformation.objects.filter(pk__in=listingnums)
    return render(request, "hello/favorites.html", {'addyinfo': addyinfo})

def about(request):
    return render(request, "hello/about.html")

def create_acc(request):
    return render(request, "hello/create_acc.html")

def login_home(request):
    return render(request, "hello/login_home.html")


def search_listings(request):
    if request.method == "POST":
        search = request.POST.get("search")
        minPrice = request.POST.get("minPrice")
        maxPrice = request.POST.get("maxPrice")

        

        if search == None:
            search == allinformation.objects.address()
              
        if minPrice == "":
            minPrice = 0
        if maxPrice == '':
            maxPrice = 10000
        
    
                              
        search1 = allinformation.objects.all().filter(address__contains=search, monthlyprice__range=(minPrice, maxPrice) )
        #print("test")
        return render(request, "hello/search_listings.html",{'search1': search1,})
    
    else:
        return render(request, "hello/search_listings.html",{})



def listing(request):
    addyinfo = allinformation.objects.filter(user=request.user).last()
    # addyinfo = allinformation.objects.first()
    return render(request, "hello/listing.html", {'addyinfo': addyinfo,})

def view_listing(request, listing_id):
    addyinfo = allinformation.objects.filter(id=listing_id).last()
    print("Listing ID:", listing_id)
    return render(request, "hello/view_listing.html", {'addyinfo': addyinfo,})

def edit_listing(request):
    addyinfo = allinformation.objects.filter(user=request.user).last()
    # addyinfo = allinformation.objects.first()

    return render(request, "hello/edit_listing.html", {'addyinfo': addyinfo,})

def deletelisting(request):
    allinformation.objects.filter(user=request.user).delete()
    return render(request, 'hello/home.html')

def test(request):
    allInfoDisplay = allinformation.objects.all()
    print(allInfoDisplay)
        
    return render(request, "hello/listing.html", {'allInfoDisplay': allInfoDisplay,})



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
            new_user = User.objects.create_user(uname, email, passw, first_name = first, last_name = last)
            new_user = form.save(commit=False)
            # new_user.first_name = first
            # new_user.last_name = last
            new_user.save()
            print(new_user)
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
       shome_list = allinformation.objects.all()
       return render(request, "hello/home.html", {'shome_list': shome_list})
    else:
        return render(request, "hello/create_acc.html")

def logoutuser(request):
    if request.method == "POST":
        logout(request)

        return redirect('/login_home')
    
def addFavorites(request):
    if request.method == "POST":
        listingid = request.POST.get("favorite")
        listing = allinformation.objects.filter(id = listingid).first()
        print(listing)
        if listing is not None:
            user = request.user
            Favorite(user = user, listing = listing).save()
            print(Favorite.objects.all())
            print("worked")
            return render(request, "hello/favorites.html")
        else:
            return render(request, "hello/test.html")
    else:
        return render(request, "hello/test.html")
            
            
        


# if userinfo.objects.filter(email=checkemail).exists():
#         userdata = userinfo.objects.filter(email=checkemail).values()[0]
#         print(userdata["password"])
#         if userdata["password"] == checkpassword:
#             return render(request, "hello/home.html")
#         else:
#             return render(request, "hello/create_acc.html")
#     else:
#         return render(request, "hello/test.html")
            
            
            
            
        
 
    
    
    
