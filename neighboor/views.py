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
    context = {
        "posts":posts,
        "hoods":hoods,
        "businesses":businesses,
    }
    return render(request, 'index.html', context)

def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()

            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password1=form.cleaned_data['password1']
            recipient=User(username=username,email=email)
            try:
                send_welcome_email(username,email)
                messages.success(request, f'Account has been created successfully!')
            except:
                print('error')
            return redirect('/login')
    else:
        form = RegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'users/register.html', context)



@login_required
def search_business(request):
    businesses = Business.objects.all()
    if 'business' in request.GET and request.GET['business']:
        search_term = request.GET["business"]
        searched_business = Business.search_by_name(search_term)
        print('*********',searched_business)
        message = f'{search_term}'
        context = {
            "searched_business":searched_business,
            "message":message,
            "businesses":businesses,

        }
        return render(request, 'search.html', context)
    else:
        message = "You haven't searched for any user"
        context = {
            "message":message,
        }
        return render(request, 'search.html', context)


