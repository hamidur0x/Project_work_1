# views.py
from django.shortcuts import render, redirect

from management.models import Sale

from management.models import Sale
from .forms import SaleForm


from django.db.models import Sum, F, DecimalField, ExpressionWrapper
from django.db.models.functions import TruncDate, TruncMonth

def create_sale(request):
    if request.method == "POST":
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save()      # your stock-checking save() method runs here
            return render(request, "sale_success.html", {"sale": sale})
    else:
        form = SaleForm()

    return render(request, "sale_form.html", {"form": form})


