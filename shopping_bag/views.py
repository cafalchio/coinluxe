from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from api_backend.models import CryptoCurrency
from wallet.models import CryptoAmount, Wallet
from .forms import AddToBagForm, RemoveFromBagForm
from .models import Holding
from .models import Bag
import stripe


@login_required
def get_debit(request):
    breakpoint
    shopping_bag, _ = Bag.objects.get_or_create(owner=request.user)
    holdings = Holding.objects.filter(shopping_bag=shopping_bag)
    debit = 0
    for holding in holdings:
        debit += holding.cryptocurrency.current_price
    return f"{debit:.2f}"

@login_required
def pay(request):
    user = request.user
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    shopping_bag, _ = Bag.objects.get_or_create(owner=user)
    holdings = Holding.objects.filter(shopping_bag=shopping_bag)
    line_items = []
    for holding in holdings:
        crypto = holding.cryptocurrency
        try:
            existing_product = stripe.Product.retrieve(crypto.id)
            line_items.append({
                "price": existing_product.default_price,
                "quantity": int(holding.amount),
            })
        except stripe.error.StripeError as e:
            print(f"Stripe API error: {e}")

    payment_link = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=line_items,
        mode="payment",
    )
    success_url = request.build_absolute_uri(reverse('payment_successful')) 
    cancel_url = request.build_absolute_uri(reverse('payment_cancelled'))
    payment_link = stripe.checkout.Session.create(line_items=line_items,
                                                  success_url=success_url,
                                                  cancel_url=cancel_url,
                                                  mode="payment"
                                                  )
    return HttpResponseRedirect(payment_link.url)
           

def add_to_wallet(user, crypto, amount):
    wallet, created = Wallet.objects.get_or_create(owner=user)
    if not created:
        existing_crypto = wallet.cryptocurrencies.filter(id=crypto.id).first()
        if existing_crypto:
            existing_crypto.cryptoamount_set.create(amount=amount)
        else:
            wallet.cryptocurrencies.add(crypto)
            crypto_amount = CryptoAmount(wallet=wallet, cryptocurrency=crypto, amount=amount)
            crypto_amount.save()
        wallet.save()
    return True

        
@login_required
def payment_successful(request):
    user = request.user
    shopping_bag = Bag.objects.get(owner=user)
    holdings = Holding.objects.filter(shopping_bag=shopping_bag)    
    message_items = []
    for holding in holdings:
        added = add_to_wallet(user, holding.cryptocurrency, holding.amount)
        if added:
            message_items.append({
                'crypto_name': holding.cryptocurrency.name,
                'amount': holding.amount,
            })
        holding.delete()

    subject = 'Payment Successful'
    if message_items:
        message = 'Your payment was successful. The following items have been added to your wallet:\n'
        for item in message_items:
            message += f"- {item['crypto_name']}: {item['amount']} units\n"
    else:
        message = 'Your payment was successful, but no items were added to your wallet.'

    from_email = 'mcafalchio@gmail.com'  
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)
    return render(request, "shopping_bag/payment_successful.html")


def payment_cancelled(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    return render(request, "shopping_bag/payment_cancelled.html")


@login_required(login_url="account_login")
def add_to_bag(request, pk):
    user = request.user
    crypto = get_object_or_404(CryptoCurrency, id=pk)
    shopping_bag, _ = Bag.objects.get_or_create(owner=user)
    if request.method == 'POST':
        form = AddToBagForm(request.POST)
        if form.is_valid():
            amount = float(form.cleaned_data['amount'])
            holding, created = Holding.objects.get_or_create(shopping_bag=shopping_bag, cryptocurrency=crypto)
            if created:
                holding.amount = amount
            else:
                holding.amount += amount
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
    holding = Holding.objects.filter(shopping_bag=shopping_bag, cryptocurrency=crypto).first()
    if holding is None:
        return redirect('crypto_list')
    amount = holding.amount
    if request.method == 'POST':
        form = RemoveFromBagForm(request.POST)
        if form.is_valid():
            sell_amount = form.cleaned_data['amount']
            if amount - float(sell_amount) > 0:
                amount -= float(sell_amount)
                holding.amount = amount
                holding.save()
            else:
                holding.delete() 
                amount = 0
    else:
        form = RemoveFromBagForm()
    return render(request, 'shopping_bag/sell_crypto.html', 
                  {"crypto":  crypto, "amount": amount, "form": form})



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
