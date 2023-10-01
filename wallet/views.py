from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from flask import redirect
from api_backend.models import CryptoCurrency
from wallet.models import CryptoWallet, CryptoCollection

@login_required(login_url="account_login")
def wallet_view(request):
    template_name = "wallet/wallet.html"
    user = request.user
    wallet, _ = CryptoWallet.objects.get_or_create(owner=user)
    crypto_data = []

    for crypto_amount in CryptoCollection.objects.filter(wallet=wallet):
        crypto = crypto_amount.cryptocurrency
        amount = crypto_amount.amount

        if amount <= 0:
            continue

        value = crypto.current_price
        value_eur = f"{amount * value:.2f} €"
        
        crypto_data.append({
            'crypto': crypto,
            'amount': amount,
            'value': value_eur,
        })

    context = {'crypto_data': crypto_data}
    return render(request, template_name, context)


@login_required(login_url="account_login")
def withdrawal(request, pk):
    user = request.user
    wallet = CryptoWallet.objects.filter(owner=user).first()
    crypto = CryptoCurrency.objects.filter(id=pk).first()
    crypto_amounts = CryptoCollection.objects.filter(wallet=wallet)
    for crypto_amount in crypto_amounts:
        if crypto_amount.cryptocurrency == crypto:
            crypto_amount.delete()

    return redirect("wallet")