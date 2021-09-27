from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render
from awards.forms import CustomUserChangeForm, SignUpForm, RatesUploadForm, ProfileUpdateForm, ProjectUploadForm, CustomUserCreationForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.shortcuts import get_object_or_404, render,redirect, resolve_url
from django.http import HttpResponse
from .serializers import ProfileSerializer, ProjectSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .signals import *








# Create your views here.

def signup(request):
    if request.method == 'POST':     
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username} Your account was created successfully. ')
            return redirect('profile')
    else:
        form = SignUpForm

    return render(request, 'registrations/signup.html', {'form':form,'registered': False } )
@login_required
def home(request):
    projects = Project.objects.all().order_by('-pk')
    return render(request, 'award/index.html',{'projects': projects})



@login_required
def profile(request):
    title = 'Your Profile'
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your profile has been updated successfully.')
            return redirect('home')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'title': title,
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, 'award/profile.html', context)


@login_required
def UserProfile(request):
    current_user = request.user


    return render(request, 'award/profile_details.html', {'current_user': current_user})


@login_required
def UploadProject(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectUploadForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
            return redirect(home)
    else:
        form = ProjectUploadForm()
        return render(request, 'award/upload_project.html', {'form':form})

# Profile related methods and views
@api_view(['GET'])
def profileList(request):
    profiles = Profile.objects.all()
    serializers = ProfileSerializer(profiles, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def profileDetail(request, pk):
    profile = Profile.objects.get(id=pk)
    serializers = ProfileSerializer(profile, many=False)
    return Response(serializers.data)

@api_view(['POST'])
def profileCreate(request):
    serializers = ProfileSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)
    
@api_view(['PUT'])
def profileUpdate(request, pk):
    profile = Profile.objects.get(id=pk)
    serializers = ProfileSerializer(instance=profile, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['DELETE'])
def profileDelete(request, pk):
    profile = Profile.objects.get(id=pk)
    profile.delete()
    return Response('Profile deleted successfully')

# Project related views and methods
@api_view(['GET'])
def projectList(request):
    projects = Project.objects.all()
    serializers = ProjectSerializer(projects, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def projectDetail(request, pk):
    project = Project.objects.get(id=pk)
    serializers = ProjectSerializer(project, many=False)
    return Response(serializers.data)

@api_view(['POST'])
def projectCreate(request):
    serializers = ProjectSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)
    
@api_view(['PUT'])
def projectUpdate(request, pk):
    project = Project.objects.get(id=pk)
    serializers = ProfileSerializer(instance=project, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['DELETE'])
def projectDelete(request, pk):
    project = Project.objects.get(id=pk)
    project.delete()
    return Response('Project deleted successfully')



