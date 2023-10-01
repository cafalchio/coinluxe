from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from wallet.models import CryptoAmount, Wallet

@login_required(login_url="account_login")
def wallet_view(request):
    template_name = "wallet/wallet.html"
    user = request.user
    wallet, _ = Wallet.objects.get_or_create(owner=user)
    crypto_data = []

    for crypto_amount in CryptoAmount.objects.filter(wallet=wallet):
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
def withdraw(request, pk):
    template_name = "wallet/wallet.html"
    user = request.user
    wallet = get_object_or_404(Wallet, owner=user)
    crypto_amount = get_object_or_404(CryptoAmount, pk=pk, wallet=wallet)
    crypto_amount.delete()
    return render(request, template_name, {'wallet': wallet})