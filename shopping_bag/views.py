from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
import stripe
from api_backend.models import CryptoCurrency
from .forms import AddToBagForm, RemoveFromBagForm
from .models import ToPay
from .models import Holding
from .models import Bag



@login_required
def get_debit(request):
    user = request.user
    debit = ToPay.objects.filter(user=user).first()
    return debit.amount if debit else 0.00


# https://www.youtube.com/watch?v=hZYWtK2k1P8&t=222s

@login_required(login_url="login")
def add_debit(request):
    # stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    # metadata = {"user_id": str(request.user.id)}
    # if request.method == "POST":
    #     checkout_session = stripe.checkout.Session.create(
    #         payment_method_types=["card"],
    #         line_items=[
    #             {
    #                 "price": settings.PRODUCT_PRICE,
    #                 "quantity": 1,
    #             },
    #         ],
    #         mode="payment",
    #         customer_creation="always",
    #         success_url=settings.REDIRECT_DOMAIN
    #         + "/payment_successful?session_id={CHECKOUT_SESSION_ID}",
    #         cancel_url=settings.REDIRECT_DOMAIN + "/payment_cancelled",
    #         metadata=metadata,
    #     )
    #     return redirect(checkout_session.url, code=303)
    return render(request, "shopping_bag/bag.html")


def payment_successful(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    checkout_session_id = request.GET.get("session_id", None)
    session = stripe.checkout.Session.retrieve(checkout_session_id)
    customer = stripe.Customer.retrieve(session.customer)
    if settings.DEBUG:
        print(f"{session} -> Session ID")
        print(f"{customer} -> costumer ")
    return render(request,
                  "shopping_bag/payment_successful.html",
                  {"customer": customer})


def payment_cancelled(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    return render(request, "shopping_bag/payment_cancelled.html")


@csrf_exempt
def stripe_webhook(request):
    # stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    # payload = request.body
    # signature_header = request.META["HTTP_STRIPE_SIGNATURE"]
    # event = None
    # try:
    #     event = stripe.Webhook.construct_event(
    #         payload, signature_header, settings.STRIPE_WEBHOOK_SECRET_TEST
    #     )
    # except ValueError:
    #     return HttpResponse(status=400)
    # except stripe.error.SignatureVerificationError:
    #     return HttpResponse(status=400)

    # if event["type"] == "checkout.session.completed":
    #     session = event["data"]["object"]
    #     session_id = session.get("id", None)
    #     time.sleep(1)
    #     line_items = stripe.checkout.Session.list_line_items(session_id,
    #                                                          limit=1)
    #     item = line_items.data[0]
    #     value = int(item.amount_total) / 100
    #     debit.amount += Decimal(value)
    #     debit.save()
    return HttpResponse(status=200)


@login_required(login_url="account_login")
def add_to_bag(request, pk):
    user = request.user
    crypto = get_object_or_404(CryptoCurrency, id=pk)
    shopping_bag, _ = Bag.objects.get_or_create(owner=user)
    if request.method == 'POST':
        form = AddToBagForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            price = crypto.current_price * float(amount)
            holding, created = Holding.objects.get_or_create(shopping_bag=shopping_bag, cryptocurrency=crypto)
            if created:
                holding.amount = price
            else:
                holding.amount += price
            holding.save()
            return redirect('bag')
    else:
        form = AddToBagForm()
    return render(request, 'shopping_bag/buy_crypto.html',
                  {'form': form, 'crypto': crypto})


@login_required(login_url="account_login")
def remove_crypto(request, pk):
    user = request.user
    crypto = get_object_or_404(CryptoCurrency, id=pk)
    shopping_bag, _ = Bag.objects.get_or_create(owner=user)
    holdings = Holding.objects.filter(shopping_bag=shopping_bag, cryptocurrency=crypto)
    if request.method == 'POST':
        form = RemoveFromBagForm(request.POST)
        if form.is_valid():
            sell_amount = form.cleaned_data['amount']
            if holdings.amount - float(sell_amount) > 0:
                holdings.amount -= float(sell_amount)
            elif holdings.amount - float(sell_amount) == 0:
                Holding.objects.filter(shopping_bag=shopping_bag, cryptocurrency=crypto).delete()
            else:
                form.add_error('amount', 'Insufficient funds')  
            holdings.save()
    else:
        form = RemoveFromBagForm()
    return render(request, 'shopping_bag/sell_crypto.html', 
                {"crypto":  crypto})



@login_required(login_url="account_login")
def shopping_bag_view(request):
    template_name = "shopping_bag/bag.html"
    user = request.user
    shopping_bag, _ = Bag.objects.get_or_create(owner=user)
    crypto_data = []
    holdings = Holding.objects.filter(shopping_bag=shopping_bag)
    for holding in holdings:
        if holding.amount <= 0:
            continue
        value = holding.cryptocurrency.current_price
        value_eur = f"{holding.amount * value:.2f} €"
        crypto_data.append({
            'crypto': holding.cryptocurrency,
            'amount': holding.amount,
            'f_amount': holding.formatted_amount,
            'value': value_eur,
        })
    context = {'crypto_data': crypto_data}
    return render(request, template_name, context)