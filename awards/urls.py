from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('', views.home, name='home'),
    path('upload-project/', views.UploadProject, name='project-upload'),
    path('myprofile/', views.UserProfile, name='myprofile'),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('projects', views.ProjectList.as_view(), name = 'projects'),
    path('project/<int:id>', views.ProjectDetailView.as_view(), name = 'project'),

    path('login/', LoginView.as_view(template_name='registrations/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registrations/logout.html'), name='logout'),
    path('search/', views.search, name= 'search'),
   
]
