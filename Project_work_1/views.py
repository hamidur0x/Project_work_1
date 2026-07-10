from django.shortcuts import render

from inventory.models import Product
from management.models import Sale

from django.db.models import Sum, F, DecimalField, ExpressionWrapper
from django.db.models.functions import TruncDate, TruncMonth


def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def report_view(request):

    # All transactions
    sales = Sale.objects.all().order_by('-sold_at')


    # Daily report
    daily_sales = (
        Sale.objects
        .annotate(date=TruncDate("sold_at"))
        .values("date")
        .annotate(
            total_sales=Sum(
                ExpressionWrapper(
                    F("items__quantity") * F("items__product__price"),
                    output_field=DecimalField()
                )
            )
        )
        .order_by("-date")
    )


    # Monthly report
    monthly_sales = (
        Sale.objects
        .annotate(month=TruncMonth("sold_at"))
        .values("month")
        .annotate(
            total_sales=Sum(
                ExpressionWrapper(
                    F("items__quantity") * F("items__product__price"),
                    output_field=DecimalField()
                )
            )
        )
        .order_by("-month")
    )


    return render(request, "report.html", {
        "sales": sales,
        "daily_sales": daily_sales,
        "monthly_sales": monthly_sales,
    })