from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.db.models import Q
from django.contrib import messages
import pandas as pd
from django.contrib.auth.decorators import login_required
from .forms import AllCryptosListForm, CryptoCurrencyEditForm
from .utils import plot_chart
from .models import AllCryptosList, Coins, CryptoCurrency, PriceUpdate


class CryptoListView(ListView):
    """ Crypto list view"""
    paginate_by = 7
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        max_pages = context['paginator'].num_pages
        page_numbers = list(range(1, max_pages + 1))
        context['page_numbers'] = page_numbers
        return context


class CoinDetailView(DetailView):
    """Coin detail view"""
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
    """Manage crypto view"""
    template_name = "cryptos/manage_cryptos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@login_required
def add_crypto(request):
    """ Cannot add crypto directly as there are 3 models and many fields,
    including the historical data, so add an crypto id and the management system]
    will add the fields later """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AllCryptosListForm(request.POST)
        if form.is_valid():
            id_value = form.cleaned_data['id'].lower()
            if not AllCryptosList.objects.filter(id=id_value).exists():
                form.save()  # Save the ID to the AllCryptosList model
                messages.success(request, 'Cryptocurrency added, data will be added in the next update.')
            else:
                messages.error(request, 'Cryptocurrency with this ID already exists.')
            return redirect(reverse('crypto_list'))
        else:
            messages.error(request, 'Form Error, please try again.')
    else:
        form = AllCryptosListForm()

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

    crypto = get_object_or_404(CryptoCurrency, pk=crypto_id)
    if request.method == 'POST':
        form = CryptoCurrencyEditForm(
            request.POST, instance=crypto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated Crypto!')
            return redirect(reverse('crypto_list'))
        else:
            messages.error(request,
                           ('Failed to update crypto. '
                            'Please ensure the form is valid.'))
    else:
        form = CryptoCurrencyEditForm(instance=crypto)
        messages.info(request, f'You are editing {crypto.name}')

    template = 'cryptos/edit_crypto.html'
    context = {
        'form': form,
        'crypto': crypto,
    }
    return render(request, template, context)


@login_required
def delete_crypto(request, crypto_id):
    """ Delete a crypto from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('crypto_list'))

    crypto = get_object_or_404(CryptoCurrency, id=crypto_id)
    crypto.delete()
    crypto_id = get_object_or_404(AllCryptosList, id=crypto_id)
    crypto_id.delete()
    messages.success(request, 'Coin deleted!')
    return redirect(reverse('crypto_list'))
