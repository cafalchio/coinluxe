from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
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
    template_name = "wallet/wallet.html"
    user = request.user
    wallet = CryptoWallet.objects.filter(owner=user).first()
    crypto = CryptoCurrency.objects.filter(id=pk).first()
    crypto_amounts = CryptoCollection.objects.filter(wallet=wallet)
    message_items = []
    for crypto_amount in crypto_amounts:
        if crypto_amount.cryptocurrency == crypto:
            message_items.append({
                'crypto_name': crypto_amount.cryptocurrency.name,
                'amount': crypto_amount.amount,
            })
            crypto_amount.delete()
    if message_items:
        message = 'Your pictures was successful.\nThe following items have been withdrawal to your wallet:\n'
        for item in message_items:
            message += f"- {item['crypto_name']}: {item['amount']} units\n"
    subject = 'Withdrawal Successful'
    from_email = 'mcafalchio@gmail.com'  
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)

    return render(request, template_name)