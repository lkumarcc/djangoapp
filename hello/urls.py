from django.urls import path
from hello import views

from hello.models import LogMessage
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="hello/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("about/", views.about, name="about"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("profile/", views.profile, name="profile"),
    path("messages/", views.messages, name="messages"),
    path("log/", views.log_message, name="log"),
    path("favorites/", views.favorites, name="favorites"),
    path("listing", views.listing, name="listing"),
    path("add_listing/", views.add_listing, name="add_listing"),
    path("display/", views.display, name="display"),
    path("test/", views.test, name="test"),
    # path("all-ammenities/", views.all_ammenities, name="all_amenities")

    
    
]

urlpatterns += staticfiles_urlpatterns()