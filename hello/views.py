import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from hello.forms import LogMessageForm
from hello.models import LogMessage
from django.views.generic import ListView
from .models import Profile, addListings

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

def display(request):
    print('test')
    add = request.POST.get("address")
    cit = request.POST.get("city")
    zip = request.POST.get("zip")
    pri = request.POST.get("price")
    roo = request.POST.get("rooms")
    fil = request.POST.get("filename")
    message = add, cit, zip, pri, roo, fil
    addListings(address = add, city = cit, zip = zip, price = pri, rooms = roo).save()
    return HttpResponse(message)
    

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