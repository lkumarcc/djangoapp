from django.urls import path
from hello import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


#might need to move this into url patterns
home_list_view = views.HomeListView.as_view(
    #queryset=Shome.objects.order_by("id")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="hello/home.html",
)
    # path("home/", home_list_view, name="home"),
urlpatterns = [
    path("", views.login_home, name="login_home"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("profile/", views.profile, name="profile"),
    path("message/", views.message, name="message"),
    path("favorites/", views.favorites, name="favorites"),
    path("add_listing", views.add_listing, name="add_listing"),
    path("edit_listing/<str:pk>/", views.edit_listing, name="edit_listing"),
    path("view_listing/<int:listing_id>", views.view_listing, name="view_listing"),
    path("test/", views.test, name="test"),
    path("create_acc/", views.create_acc, name="create_acc"),
    path("login_home/", views.login_home, name="login_home"), 
    path("authenticateuser/", views.authenticateuser, name="authenticateuser"),  
    path("logoutuser/", views.logoutuser, name="logoutuser"), 
    path("search_listings/", views.search_listings, name="search_listings"), 
    path("addFavorites/", views.addFavorites, name="addFavorites"), 
    path("delete_favorite/<int:listingid>", views.delete_favorite, name="delete_favorite"), 
    path("terms_conditions/", views.terms_conditions, name="terms_conditions"), 
    path("privacy_policy/", views.privacy_policy, name="privacy_policy"), 
    # path("all-ammenities/", views.all_ammenities, name="all_amenities")

    
    
] 


urlpatterns += staticfiles_urlpatterns()


