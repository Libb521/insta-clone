from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    path('',views.welcome,name ='welcome'),
    path('newprofile/',views.profile,name = 'profile'),
    path('image/',views.add_image,name = 'upload_image'),
    path('search/',views.search,name = 'search'),
    path('showprofile/',views.display_profile,name = 'showprofile'),
    path('signup/', views.signup,name='signup'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)