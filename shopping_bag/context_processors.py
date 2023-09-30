from .models import Bag, Holding


def debit(request):
    if request.user.is_authenticated:
        shopping_bag, _ = Bag.objects.get_or_create(owner=request.user)
        holdings = Holding.objects.filter(shopping_bag=shopping_bag)
        debit = 0
        for holding in holdings:
            debit += holding.cryptocurrency.current_price
        return {"debit": debit}
    else:
        return {"debit": "0.00"}
