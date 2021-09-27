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
    path('logiiin', views.LogiiinView.as_view(), name='logiiin'),
    path('projects', views.ProjectList.as_view(), name = 'projects'),
    path('project/<int:id>', views.ProjectDetailView.as_view(), name = 'project'),

    path('login/', LoginView.as_view(template_name='registrations/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registrations/logout.html'), name='logout'),

# might not be used
    path('profile-detail/<str:pk>/', views.profileDetail, name='profile-detail'),
    path('profile-create/', views.profileCreate, name='profile-create'),
    path('profile-update/<str:pk>/', views.profileUpdate, name='profile-update'),
    path('profile-delete/<str:pk>/', views.profileDelete, name='profile-delete'),
    path('project-list/', views.projectList, name='project-list'),
    path('project-detail/<str:pk>/', views.projectDetail, name='project-detail'),
    path('project-create/', views.projectCreate, name='project-create'),
    path('project-update/<str:pk>/', views.projectUpdate, name='project-update'),
    path('project-delete/<str:pk>/', views.projectDelete, name='project-delete'),

   
]
