from django.views.generic import ListView
from api_backend.models import CryptoCurrency


# Create your views here.
class IndexListView(ListView):
    paginate_by = 10
    model = CryptoCurrency
    template_name = "home/index.html"

    def get_queryset(self):
        queryset = CryptoCurrency.objects.filter(
            market_cap__isnull=False).order_by('-market_cap')[:4]
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        if queryset is not None:
            context['top_gainers'] = queryset
        return context
