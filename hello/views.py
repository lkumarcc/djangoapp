import re
from django.utils.timezone import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from hello.forms import LogMessageForm, CreateUserForm
from hello.models import LogMessage
from django.views.generic import ListView
from .models import Profile, addListings, Shome, allinformation, Favorite
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import AddListingForm, DeleteFavorites, EditProfileForm
from django.http import HttpResponseRedirect
from django.contrib import messages

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage
    #this cant be inside here but theres nowhere else to put it, need new homepage

def home(request):
    shome_list = allinformation.objects.all()
    return render(request, 'hello/home.html', {'shome_list': shome_list})

def profile(request):
    user_listings = allinformation.objects.filter(user=request.user)
    submitted = False
    #FXME 
    user_instance = Profile.objects.get(user = request.user)
   
    form = EditProfileForm(instance=user_instance)
    if request.method =='POST':
        form = EditProfileForm(data =request.POST, files = request.FILES, instance= user_instance)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return HttpResponseRedirect('/profile?submitted=True')
    else:
        form = EditProfileForm(instance=user_instance)
        if 'submitted' in request.GET: 
            submitted = True

    return render(request, "hello/profile.html", {'user_listings': user_listings, 'form':form, 'submitted': submitted} )

def message(request):
    return render(request, "hello/message.html")

def delete_favorite(request, listingid):
    listing = Favorite.objects.get(listing_id = listingid)
    listing.delete()
    return redirect("/favorites")
    
    
    # print("test1")
    # if request.method =='POST':
    #     print("test post")
    #     # create a form instance and populate it with data from the request:
    #     form = DeleteFavorites(request.POST)
    #     # check whether it's valid:
    #     if form.is_valid():
    #         form=form.save(commit=False)
    #         listing_delete = form.cleaned_data['listing_id']
    #         print(listing_delete, "?")
    #         Favorite.objects.get(listing_id=listing_delete).delete()
    #         print(Favorite.objects.get.all())
    #         # process the data in form.cleaned_data as required
    #         # ...
    #         # redirect to a new URL:
    #         return HttpResponseRedirect('/favorites/')
    #     else:
    #         print(form.errors.as_data())
    # return HttpResponseRedirect('/favorites/')

def favorites(request):
    #handle accessing user favorites
    listingid = list(Favorite.objects.filter(user=request.user).values("listing_id"))
    listingnums = []
    for item in listingid:
        listingnums.append(item["listing_id"])
    favorite_listings = allinformation.objects.filter(pk__in=listingnums)
    
    return render(request, "hello/favorites.html", {'favorite_listings': favorite_listings, 'messages': messages})

def about(request):
    return render(request, "hello/about.html")


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

def view_listing(request, listing_id):
    addyinfo = allinformation.objects.filter(id=listing_id).last()
    print("Listing ID:", listing_id)
    return render(request, "hello/view_listing.html", {'addyinfo': addyinfo,})

def edit_listing(request, pk):
    submitted = False
    listing_object = allinformation.objects.get(id=pk)
    form = AddListingForm(instance=listing_object)
    
    if request.method =='POST':
        if 'delete_listing' in request.POST: #handle deleting listing button on edit page 
                listing = allinformation.objects.get(id=pk).delete()
                print("Deleting Listing:", listing)
                shome_list = allinformation.objects.all()
                messages= ['Your listing has been deleted successfully.']
                return render(request, 'hello/home.html', {'shome_list': shome_list, 'messages': messages})
        else:
            form = AddListingForm(data =request.POST, files = request.FILES, instance=listing_object)
            if form.is_valid():
                listing = form.save(commit=False)
                listing.user = request.user
                listing.save()
                return HttpResponseRedirect('/edit_listing/' +pk+'/?submitted=True')
        
    else:
        form = AddListingForm(instance=listing_object)
        if 'submitted' in request.GET: 
            submitted = True

    return render(request, 'hello/edit_listing.html', {'form': form, 'submitted': submitted})


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
    

def create_acc(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            user.profile.phone = request.POST['phone']
            user.profile.school = request.POST['school']
            user.profile.gender = request.POST['gender']
            login(request, user)
            messages.success(request,("Registration Successful!"))
            shome_list = allinformation.objects.all()
            return render(request, "hello/home.html", {'shome_list': shome_list})
    else:
        form = CreateUserForm() 

    return render(request, "hello/create_acc.html", {'form': form,})



# if __name__ == '__main__':
#     all_ammenities() 

#FIXME has some bugs 
def authenticateuser(request):
    if request.method == "POST":
        checkusername = request.POST.get("username")
        checkpassword = request.POST.get("password")
        user = authenticate(username=checkusername, password=checkpassword)
        if user is not None:
            login(request, user) 
            messages.info(request, f"You are now logged in as {user.username}!")
            shome_list = allinformation.objects.all()
            return render(request, "hello/home.html", {'shome_list': shome_list})
    return render(request, "hello/login_home.html")
        

def logoutuser(request):
    if request.method == "POST":
        logout(request)

        return redirect('/login_home')
    
def addFavorites(request):
    if request.method == "POST":
        #get id number
        listingid = request.POST.get("favorite")
        listing = allinformation.objects.filter(id = listingid).first()
        print(listingid, listing)
        if listing is not None:
            #check if the item exists
            user = request.user
            listingid = list(Favorite.objects.filter(user=request.user).filter(listing_id = listingid))

            #if does return error and rerender page
            if len(listingid) >= 1:
                messages.error(request, 'You have already favorited this listing.')
                return render(request, "hello/view_listing.html", {'addyinfo': listing})
            #if doesn't add listing, add success message, and redirect
            else:
                user = request.user
                Favorite(user = user, listing = listing).save()
                messages.success(request, 'Your listing has been added to favorites!')
                return render(request, "hello/view_listing.html", {'addyinfo': listing})
        else:
            return render(request, "hello/view_listing.html", {'addyinfo': listing})
    else:
        return redirect("/home")
            
            

            
            
            
        
 
    
    
    
