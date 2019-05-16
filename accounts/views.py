from django.shortcuts import render, redirect, HttpResponseRedirect, resolve_url
from django.http import JsonResponse
from django.utils.http import is_safe_url, urlsafe_base64_decode
from .forms import UserLoginForm, UserRegistrationForm
from django.template.response import TemplateResponse
from django.utils.encoding import force_text
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import password_reset
from django.contrib.auth.tokens import default_token_generator
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache


"""A view that displays the index page"""
def index(request):
    data = {'data': False}
    if request.method == "POST":
        password_reset(request,
                   template_name='registration/password_reset_form.html',
                   email_template_name='registration/password_reset_email.html',
                   subject_template_name='registration/password_reset_subject.txt',
                   password_reset_form=PasswordResetForm,
                   token_generator=default_token_generator,
                   post_reset_redirect=None,
                   from_email=None,
                   extra_context=None,
                   html_email_template_name=None)
        data['data'] = True
        return JsonResponse(data)
    else:
        login_form = UserLoginForm()
        reg_form = UserRegistrationForm()
        forg_pass_form = PasswordResetForm()
        args = {'login_form': login_form, 'reg_form': reg_form, 'forg_pass_form':forg_pass_form, 'next': request.GET.get('next', '')}
        return render(request, "index.html", args)

def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect(reverse('index'))

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

def login_from_password_change(request):
    login_from_pass_change = True
    login_form = UserLoginForm()
    reg_form = UserRegistrationForm()
    forg_pass_form = PasswordResetForm()
    args = {'login_from_pass_change': login_from_pass_change, 'login_form': login_form, 'reg_form': reg_form, 'forg_pass_form':forg_pass_form, 'next': request.GET.get('next', '')}
    return render(request, "index.html", args)

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


@sensitive_post_parameters()
@never_cache
def password_reset_confirm(request, uidb64=None, token=None,
                           template_name='registration/password_reset_confirm.html',
                           token_generator=default_token_generator,
                           set_password_form=SetPasswordForm,
                           post_reset_redirect=None,
                           current_app=None, extra_context=None):
    """
    View that checks the hash in a password reset link and presents a
    form for entering a new password.
    """
    login_form = UserLoginForm()
    UserModel = get_user_model()
    assert uidb64 is not None and token is not None  # checked by URLconf
    if post_reset_redirect is None:
        post_reset_redirect = reverse('password_reset_complete')
    else:
        post_reset_redirect = resolve_url(post_reset_redirect)
    try:
        # urlsafe_base64_decode() decodes to bytestring on Python 3
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserModel._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        validlink = True
        if request.method == 'POST':
            form = set_password_form(user, request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(post_reset_redirect)
        else:
            form = set_password_form(user)
    else:
        validlink = False
        form = None
    context = {
        'login_form': login_form,
        'form': form,
        'validlink': validlink,
    }
    if extra_context is not None:
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app

    return TemplateResponse(request, template_name, context)