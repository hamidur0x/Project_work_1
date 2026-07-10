from django.shortcuts import render, redirect
from .forms import SaleItemForm
from .models import Sale, SaleItem
from inventory.models import Product


def create_sale(request):

    error = None

    cart = request.session.get("cart", [])

    form = SaleItemForm()   # FIX: always create form


    if request.method == "POST":

        action = request.POST.get("action")


        # Add item to cart
        if action == "add":

            form = SaleItemForm(request.POST)

            if form.is_valid():

                product = form.cleaned_data["product"]
                quantity = float(form.cleaned_data["quantity"])


                cart.append({
                    "product_id": product.id,
                    "name": product.name,
                    "quantity": quantity,
                    "price": float(product.price),
                    "subtotal": quantity * float(product.price)
                })


                request.session["cart"] = cart

                # clear form after adding
                form = SaleItemForm()



        # Complete sale
        elif action == "complete":

            try:

                sale = Sale.objects.create()


                for item in cart:

                    product = Product.objects.get(
                        id=item["product_id"]
                    )


                    SaleItem.objects.create(
                        sale=sale,
                        product=product,
                        quantity=item["quantity"]
                    )


                # empty cart
                request.session["cart"] = []


                return redirect("create_sale")


            except ValueError as e:

                error = str(e)



    total = sum(
        item["subtotal"]
        for item in cart
    )


    return render(
        request,
        "sale_form.html",
        {
            "form": form,
            "cart": cart,
            "total": total,
            "error": error
        }
    )