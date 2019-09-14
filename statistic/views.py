from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from bugs.models import Bug
from features.models import Feature


@login_required
def all_data(request):
    # A view which shows charts and diagrams
    if request.user.is_authenticated:
        bugs = Bug.objects.all()
        features = Feature.objects.all()
        args = {
            "bugs": bugs,
            "features": features,
        }
        return render(request, "statistic.html", args)
    else:
        return redirect('index')
