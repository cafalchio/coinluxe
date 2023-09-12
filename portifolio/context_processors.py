from portifolio.models import Credits


def credits(request):
    if request.user.is_authenticated:
        credits_obj = Credits.objects.filter(user=request.user).first()
        if credits_obj is None:
            credits = "0.00"
        else:
            credits = credits_obj.amount
        return {"credits": credits}
    else:
        return {"credits": "0.00"}
