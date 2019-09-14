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
        # All the bugs and Features
        qs_bugs = Bug.objects.all()
        qs_features = Feature.objects.all()
        # The number of bugs and features
        bugs_numbers = qs_bugs.count()
        features_numbers = qs_features.count()
        # Labels
        labels_tickets = ['Bugs', 'Features']
        # The number of upvotes of all bugs and features
        bug_upvotes = 0
        feature_upvotes = 0
        for bug in qs_bugs:
            bug_upvotes += bug.upvotes.count()
        for feature in qs_features:
            feature_upvotes += feature.upvotes
        # Datasets
        tickets = [bugs_numbers, features_numbers]
        upvotes = [bug_upvotes, feature_upvotes]
        data = {
            "labels_tickets": labels_tickets,
            "tickets": tickets,
            "upvotes": upvotes,
        }
        return Response(data)
