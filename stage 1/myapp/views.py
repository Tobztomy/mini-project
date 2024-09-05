from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib import messages
from datetime import date as date, datetime as dt
from .models import *
from django.db.models import Q, Min, Max
# Create your views here.


def index(request):
    return render(request, 'index.html')

# ----------customerSignup--------------------------------


def customerSignup(request):
    if request.POST:
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        phone = request.POST['phone']
        place = request.POST['place']
        image = request.FILES["image"]
        password = request.POST['password']

        log = Login.objects.create_user(
            username=email,
            password=password,
            view_password=password,
            is_active=0,
            user_type='Customer')
        log.save()
        reguser = Customer.objects.create(
            loginId=log,
            firstName=firstName,
            lastName=lastName,
            email=email,
            phone=phone,
            place=place,
            image=image,)
        reguser.save()
        messages.success(request, "Registration Successful Wait For Approval")
        return redirect('/login')
    return render(request, 'signup.html')


def sellerSignup(request):
    if request.POST:
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        phone = request.POST['phone']
        place = request.POST['place']
        image = request.FILES["image"]
        password = request.POST['password']

        log = Login.objects.create_user(
            username=email,
            password=password,
            view_password=password,
            is_active=0,
            user_type='Seller')
        log.save()
        reguser = Seller.objects.create(
            loginId=log,
            firstName=firstName,
            lastName=lastName,
            email=email,
            phone=phone,
            place=place,
            image=image,)
        reguser.save()
        messages.success(request, "Registration Successful Wait For Approval")
        return redirect('/login')
    return render(request, 'signup.html')


def login(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.user_type == 'admin':
                messages.success(request, 'Welcome to Retrobid')
                return redirect('/adminHome')
            elif user.user_type == 'Customer':
                request.session['uid'] = user.id
                messages.success(request, 'Welcome to Retrobid')
                return redirect('/customerHome')
            elif user.user_type == 'Seller':
                request.session['uid'] = user.id
                messages.success(request, 'Welcome to Retrobid')
                return redirect('/sellerHome')
            else:
                messages.success(request, 'Invalid')
        else:
            messages.success(request, 'Invalid')
    return render(request, 'login.html')

