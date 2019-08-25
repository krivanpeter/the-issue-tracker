from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Package


@login_required
def all_packages(request):
    # A view which shows all the news
    if request.user.is_authenticated:
        packages = Package.objects.all()
        return render(request, 'packages.html', {'packages': packages})
    else:
        return redirect('index')