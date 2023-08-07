from django.shortcuts import redirect, render, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.db.models import Q
from django.contrib import messages
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.core.management import call_command

from .forms import CryptoCurrencyForm
from .utils import plot_chart
from .models import Coins, CryptoCurrency, PriceUpdate


class CryptoListView(ListView):
    paginate_by = 10
    model = CryptoCurrency
    template_name = "api_backend/cryptos.html"

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
    template_name = "api_backend/coin.html"

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
    template_name = "api_backend/manage_cryptos.html"
    
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
                messages.success(request, message)
            except:
                messages.error(request, "Coin could not be added, try again later.")
            return redirect(reverse('crypto_list'))
        else:
            messages.error(request,'Form Error, please try again.')
    else:
        
        form = CryptoCurrencyForm()

    template = 'api_backend/add_crypto.html'
    context = {
        'form': form,
    }

    return render(request, template, context)