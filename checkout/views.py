from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils import timezone
from accounts.models import UserProfile
from attractor import settings
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
import stripe
from packages.models import Package


stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    user = UserProfile.objects.get(user__username=request.user.username)
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                package = get_object_or_404(Package, pk=id)
                total += quantity * package.price
                order_line_item = OrderLineItem(
                    order=order,
                    package=package,
                    quantity=quantity
                )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="GBP",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, 'Your card was declined!')
            if 'customer' in locals():
                if customer.paid:
                    for id, quantity in cart.items():
                        package = get_object_or_404(Package, pk=id)
                        user.available_upvotes += quantity * package.worth_upvotes
                        user.save()
                    request.session['cart'] = {}
                    messages.success(
                        request, 'Your purchase has been successful.',
                        fail_silently=True)
                    return redirect('view_profile', username=request.user)
                else:
                    messages.error(request, 'Unable to take payment.')
            else:
                messages.error(request, "An error occurred")
                return redirect("checkout")
        else:
            messages.error(
                request,
                'We were unable to take a payment with that card!')
    else:
        if not request.session.get('cart', {}):
            return redirect(reverse('view_cart'))
        order_form = OrderForm(
            initial={
                'full_name': request.user.first_name + ' ' + request.user.last_name,
                'phone_number': user.phone_number,
                'country': user.phone_number,
                'postcode': user.postcode,
                'town_or_city': user.town_or_city,
                'street_address1': user.street_address1,
                'street_address2': user.street_address2,
            })
        payment_form = MakePaymentForm()
    return render(request, 'checkout.html', {
        'order_form': order_form,
        'payment_form': payment_form,
        'publishable': settings.STRIPE_PUBLISHABLE})
