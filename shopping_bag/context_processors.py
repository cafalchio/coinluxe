from .models import ToPay
import logging

logger = logging.getLogger("django")


def debit(request):
    if request.user.is_authenticated:
        try:
            debit_obj = ToPay.objects.filter(user=request.user).first()
            debit = debit_obj.amount
        except Exception as e:
            logger.info(f"{'*' * 30}Custom Error:\nNo user registered {e}, type {type(e)}")
            debit = "0.00"
        
        return {"debit": debit}
    else:
        return {"debit": "0.00"}
