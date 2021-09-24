from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile-list/', views.profileList, name='profile-list'),
    path('profile-detail/<str:pk>/', views.profileDetail, name='profile-detail'),

   
]
