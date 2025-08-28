# Create your views here.
from django.http import HttpResponse
from django.db import transaction
from .models import Account

@transaction.atomic
def transfer_money(request):
    # Example: Transfer 100 from A to B atomically
    try:
        acc1 = Account.objects.get(name="Alice")
        acc2 = Account.objects.get(name="Bob")

        acc1.balance -= 100
        acc1.save()

        # Simulate an error (uncomment to test rollback)
        # raise Exception("Something went wrong!")

        acc2.balance += 100
        acc2.save()

        return HttpResponse("✅ Transfer Successful!")

    except Exception as e:
        return HttpResponse(f"❌ Transfer Failed: {e}")
