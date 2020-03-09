from django.urls import path
from . import views

urlpatterns=[
    path('',views.welcome,name ='welcome'),
    path('newprofile/',views.profile,name = 'profile'),
    path('image/',views.add_image,name = 'upload_image'),
    path('search/',views.search,name = 'search'),
    path('showprofile/',views.display_profile,name = 'showprofile'),
    ]