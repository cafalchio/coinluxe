from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from wallet.models import Wallet

@login_required(login_url="account_login")
def wallet_view(request):
    template_name = "wallet/wallet.html"
    user = request.user
    wallets, _ = Wallet.objects.get_or_create(owner=user)
    crypto_data = []
    
    for wallet in wallets.cryptocurrency.all():
        if wallet.amount <= 0:
            continue
        value = wallet.cryptocurrency.current_price
        value_eur = f"{wallet.amount * value:.2f} €"
        crypto_data.append({
            'crypto': wallet.cryptocurrency,
            'amount': wallet.amount,
            'f_amount': wallet.formatted_amount,
            'value': value_eur,
        })

    context = {'crypto_data': crypto_data}
    return render(request, template_name, context)