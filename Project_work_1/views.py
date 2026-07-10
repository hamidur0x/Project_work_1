from django.shortcuts import render

from inventory.models import Product
from management.models import Sale

from django.db.models import Sum, F, DecimalField, ExpressionWrapper
from django.db.models.functions import TruncDate, TruncMonth



def home(request):

    products = Product.objects.all()

    return render(
        request,
        "index.html",
        {
            "products": products
        }
    )



def report_view(request):

    sales = Sale.objects.all().order_by("-date")


    # Daily report
    daily_sales = (
        Sale.objects
        .annotate(
            day=TruncDate("date")
        )
        .values("day")
        .annotate(
            total_sales=Sum(
                ExpressionWrapper(
                    F("quantity") * F("product__price"),
                    output_field=DecimalField()
                )
            )
        )
        .order_by("-day")
    )


    # Monthly report
    monthly_sales = (
        Sale.objects
        .annotate(
            month=TruncMonth("date")
        )
        .values("month")
        .annotate(
            total_sales=Sum(
                ExpressionWrapper(
                    F("quantity") * F("product__price"),
                    output_field=DecimalField()
                )
            )
        )
        .order_by("-month")
    )


    return render(
        request,
        "report.html",
        {
            "sales": sales,
            "daily_sales": daily_sales,
            "monthly_sales": monthly_sales,
        }
    )