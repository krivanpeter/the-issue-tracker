from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from bugs.models import Bug
from features.models import Feature


@login_required
def statistic(request):
    # A view which shows charts and diagrams
    if request.user.is_authenticated:
        return render(request, "statistic.html")
    else:
        return redirect('index')


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_bugs = Bug.objects.all().count()
        qs_features = Feature.objects.all().count()
        labels = ['Bugs', 'Features']
        default_items = [qs_bugs, qs_features ]
        data = {
            "labels": labels,
            "default": default_items
        }
        return Response(data)
