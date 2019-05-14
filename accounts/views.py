from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    """A view that displays the index page"""
    login_form = UserLoginForm()
    reg_form = UserRegistrationForm()
    args = {'login_form': login_form, 'reg_form': reg_form, 'next': request.GET.get('next', '')}
    return render(request, "index.html", args)


def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))

def authentication(request):
    user_form = UserLoginForm(request.POST)
    if user_form.is_valid():
        print("VALID")
        user = auth.authenticate(request.POST['username_or_email'],
                                 password=request.POST['password'])
        if user:
            auth.login(request, user)
            messages.success(request, "You have successfully logged in")
            if request.GET and request.GET['next'] !='':
                next = request.GET['next']
                return HttpResponseRedirect(next)
            else:
                return redirect(reverse('index'))
        else:
            data = {
                'username_or_password_error': True
            }
            return JsonResponse(data)
    return index(request)

def login(request):
    data = {'username_or_password_error': False}
    """A view that manages the login form"""
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])
            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully logged in")
                return JsonResponse(data)
            else:
                data['username_or_password_error'] = True
                return JsonResponse(data)
    else:
        user_form = UserLoginForm()
    return index(request)


@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""
    return render(request, 'profile.html')

def check_username(request):
    username = request.GET.get('username', None)
    data = {
        'username_is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)
    
def check_email(request):
    email = request.GET.get('email', None)
    data = {
        'email_is_taken': User.objects.filter(email__iexact=email).exists()
    }
    return JsonResponse(data)
    
def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))

            else:
                messages.error(request, "Unable to log you in at this time!")
        else:
            return login(request)
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'register.html', args)

