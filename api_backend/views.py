from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.db.models import Q
from django.contrib import messages
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.core.management import call_command

from .forms import CryptoCurrencyEditForm, CryptoCurrencyForm
from .utils import plot_chart
from .models import Coins, CryptoCurrency, PriceUpdate


class CryptoListView(ListView):
    paginate_by = 10
    model = CryptoCurrency
    template_name = "cryptos/cryptos.html"

    def get_queryset(self):
        queryset = CryptoCurrency.objects.order_by('-market_cap')
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(symbol__icontains=search_query)
            )
        return queryset


class CoinDetailView(DetailView):
    model = Coins
    template_name = "cryptos/crypto_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get models data
        coin = Coins.objects.get(id=self.kwargs.get("pk"))
        price = PriceUpdate.objects.get(id=coin.id)
        crypto = CryptoCurrency.objects.get(id=coin.id)

        # processing data
        df = pd.DataFrame(price.formatted_price_time)
        df.columns = ["date", "price"]
        df.date = pd.to_datetime(df.date, unit='ms')
        chart = plot_chart(df)

        # contexts
        context['chart'] = chart
        context['coin'] = coin
        context['crypto'] = crypto

        return context


class ManageCryptos(TemplateView):
    template_name = "cryptos/manage_cryptos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@login_required
def add_crypto(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CryptoCurrencyForm(request.POST, request.FILES)
        if form.is_valid():
            coin_id = form.cleaned_data['id']
            try:
                message = call_command('update_coins', coin=coin_id)
            except:
                messages.error(request, message)
            try:
                messages.success(request, message)
            except:
                messages.error(request, message)
            try:
                message = call_command('update_coins_charts', coin=coin_id)
            except:
                messages.error(request, message)
            return redirect(reverse('crypto_list'))
        else:
            messages.error(request, 'Form Error, please try again.')
    else:

        form = CryptoCurrencyForm()

    template = 'cryptos/add_crypto.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_crypto(request, crypto_id):
    """ Edit a cryptocurrency in the crypto store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(CryptoCurrency, pk=crypto_id)
    if request.method == 'POST':
        form = CryptoCurrencyEditForm(
            request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated Crypto!')
            return redirect(reverse('coin', pk=crypto_id))
        else:
            messages.error(request,
                           ('Failed to update crypto. '
                            'Please ensure the form is valid.'))
    else:
        form = CryptoCurrencyEditForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'cryptos/edit_crypto.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_crypto(request, crypto_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('crypto_list'))

    crypto = get_object_or_404(CryptoCurrency, id=crypto_id)
    crypto.delete()
    messages.success(request, 'Coin deleted!')
    return redirect(reverse('crypto_list'))
