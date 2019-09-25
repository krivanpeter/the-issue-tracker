from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from bugs.models import Bug
from features.models import Feature
from checkout.models import OrderLineItem
from packages.models import Package


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
        qs_orders = OrderLineItem.objects.all()
        qs_packages = Package.objects.all()

        # The prices of different packages
        package_prices = [0, 0, 0]
        for idx, package in enumerate(qs_packages):
            package_prices[idx] = package.price

        # The number of orders of packages
        bought_packs = [0, 0, 0]
        spent_money = [0, 0, 0]
        for order in qs_orders:
            if order.package.title == 'Bronze Pack':
                bought_packs[0] += 1
                spent_money[0] += package_prices[0]
            elif order.package.title == 'Silver Pack':
                bought_packs[1] += 1
                spent_money[1] += package_prices[1]
            else:
                bought_packs[2] += 1
                spent_money[2] += package_prices[2]

        # The number of bugs and features
        bugs_numbers = qs_bugs.count()
        features_numbers = qs_features.count()

        # Labels
        labels_packs = ['Bronze Pack', 'Silver Pack', 'Gold Pack']
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
            "labels_packs": labels_packs,
            "tickets": tickets,
            "upvotes": upvotes,
            "bought_packs": bought_packs,
            "spent_money": spent_money,
        }
        return Response(data)
