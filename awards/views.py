from django.shortcuts import render
from awards.forms import SignUpForm, RatesUploadForm, ProfileUpdateForm, ProjectUploadForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.shortcuts import get_object_or_404, render,redirect, resolve_url
from django.http import HttpResponse
from .serializers import ProfileSerializer, ProjectSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view




# Create your views here.

def signup(request):
    if request.method == 'POST':     
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username} Your account was created successfully. ')
            return redirect('home')
    else:
        form = SignUpForm

    return render(request, 'registration/signup.html', {'form':form,'registered': False } )

def home(request):
    return render(request, 'award/index.html')

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
    
@api_view(['POST'])
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
def projectList(self, request):
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
    
@api_view(['POST'])
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



