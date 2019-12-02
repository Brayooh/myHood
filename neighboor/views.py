from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import *
from .emails import send_welcome_email
from rest_framework.response import Response
from rest_framework.views import APIView


@login_required
def home(request):
    posts = Post.objects.all()
    hoods = Neighborhood.objects.all()
    businesses = Business.objects.all()
 
    return render(request, 'index.html', context)

