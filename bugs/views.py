from django.shortcuts import render
from .models import Bug
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def all_bugs(request):
    users = User.objects.all()
    bugs = Bug.objects.all()
    return render(request, "bugs.html", {"bugs": bugs, "users": users})
