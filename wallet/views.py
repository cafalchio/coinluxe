from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from shopping_bag.models import Holding
from wallet.models import Wallet

@login_required(login_url="account_login")
def wallet_view(request):
    template_name = "shopping_bag/wallet.html"
    user = request.user
    shopping_bag, _ = Wallet.objects.get_or_create(owner=user)
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