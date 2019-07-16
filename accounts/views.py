from django.shortcuts import (
    render,
    redirect,
    HttpResponseRedirect,
    resolve_url
)
from django.contrib.auth.forms import (
    PasswordResetForm,
    SetPasswordForm,
    PasswordChangeForm
)
from .forms import (
    UserLoginForm,
    UserRegistrationForm,
    EditProfileForm,
    EditUserForm
)
from django.http import JsonResponse, Http404
from django.utils.http import urlsafe_base64_decode
from django.template.response import TemplateResponse
from django.utils.encoding import force_text
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import password_reset
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from bugs.models import Bug


"""A view that displays the index page"""
def index(request):
    data = {'data': False}
    if request.method == "POST":
        if 'reset_password' in request.POST:
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
        elif 'create_new_account' in request.POST:
            return register(request)
        elif 'login' in request.POST:
            return login(request)
    else:
        if request.user.is_authenticated():
            return redirect('news')
        login_form = UserLoginForm()
        reg_form = UserRegistrationForm()
        forg_pass_form = PasswordResetForm()
        args = {'login_form': login_form, 'reg_form': reg_form, 'forg_pass_form':forg_pass_form, 'next': request.GET.get('next', '')}
        return render(request, "index.html", args)


"""
A view checks the user's username and password
If correct redirect to page of the logged in users
"""
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
                return redirect('news')
            else:
                data['username_or_password_error'] = True
                return JsonResponse(data)
        else:
            return redirect('index')
    else:
        return index(request)


"""
A view checks the user's username and password
Necessary to be able to prevent the submiting of the loginform
if user's data are incorrect
"""
def check_userdata(request):
    if request.method == "POST":
        data = {'username_or_password_error': False}
        username_or_email = request.POST.get('username_or_email', None)
        password = request.POST.get('password', None)
        user = auth.authenticate(username_or_email, password=password)
        if user:
            data['username_or_password_error'] = False
            return JsonResponse(data)
        else:
            data['username_or_password_error'] = True
            return JsonResponse(data)
    else:
        raise Http404()


"""A view which logouts the user"""
def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect('index')


"""
A view which let the user to login after changed password
"""
def login_from_password_change(request):
    if request.method == "POST":
        return login(request)
    else:
        login_from_pass_change = True
        login_form = UserLoginForm()
        reg_form = UserRegistrationForm()
        forg_pass_form = PasswordResetForm()
        args = {'login_from_pass_change': login_from_pass_change, 'login_form': login_form,
                'reg_form': reg_form, 'forg_pass_form': forg_pass_form, 'next': request.GET.get('next', '')}
        return render(request, "index.html", args)


"""A view that displays the profile page of a logged in user"""
@login_required
def view_profile(request):
    if Bug.objects.filter(reported_by=request.user.userprofile).exists():
        bugs = Bug.objects.filter(reported_by=request.user.userprofile)
        args = {
            'user': request.user,
            'bugs': bugs
        }
    else:
        args = {
            'user': request.user
        }
    return render(request, 'profile.html', args)


"""A view that lets a logged in user to change the profile"""
@login_required
def edit_profile(request):
    if request.method == "POST":
        user_form = EditProfileForm(request.POST, instance=request.user)
        profile_form = EditUserForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            profile_form.avatar = profile_form.cleaned_data['avatar']
            user_form.save()
            profile_form.save()
            return redirect('/profile/')
        else:
            return redirect('/profile/edit')
    else:
        user_form = EditProfileForm(instance=request.user)
        profile_form = EditUserForm(instance=request.user.userprofile)
        args = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'editprofile.html', args)


"""A view that lets a logged in user to change the profile"""
@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/profile/')
        else:
            return redirect('/profile/change-password/')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'change_password.html', args)


"""A view that checks if username exists in database"""
def check_username(request):
    if request.method == "GET":
        username = request.GET.get('username', None)
        data = {
            'username_is_taken': User.objects.filter(username__iexact=username).exists()
        }
        return JsonResponse(data)
    else:
        raise Http404()


"""A view that checks if email address exists in database"""
def check_email(request):
    if request.method == "GET":
        email = request.GET.get('email', None)
        data = {
            'email_is_taken': User.objects.filter(email__iexact=email).exists()
        }
        return JsonResponse(data)
    else:
        raise Http404()


"""A view that manages the registration form"""
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect('news')

            else:
                messages.error(request, "Unable to log you in at this time!")
                return redirect('index')
        else:
            return login(request)
    else:
        raise Http404()


"""
View that checks the hash in a password reset link and presents a
form for entering a new password.
(Code from django's webpage.
Slightly changed: login form added to it)
"""
@sensitive_post_parameters()
@never_cache
def password_reset_confirm(request, uidb64=None, token=None,
                           template_name='registration/password_reset_confirm.html',
                           token_generator=default_token_generator,
                           set_password_form=SetPasswordForm,
                           post_reset_redirect=None,
                           current_app=None, extra_context=None):
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