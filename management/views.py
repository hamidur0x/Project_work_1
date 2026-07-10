from django.shortcuts import render, redirect

from .forms import SaleForm
from .models import Sale

from inventory.models import Product



def create_sale(request):

    cart = request.session.get("cart", [])

    error = None



    if request.method == "POST":

        action = request.POST.get("action")



        # Add item to cart
        if action == "add":

            form = SaleForm(request.POST)


            if form.is_valid():

                product = form.cleaned_data["product"]

                quantity = form.cleaned_data["quantity"]



                if quantity <= 0:

                    error = "Quantity must be greater than zero."



                elif quantity > product.stock:

                    error = "Not enough stock available."



                else:

                    item = {

                        "id": product.id,

                        "name": product.name,

                        "quantity": quantity,

                        "price": float(product.price),

                        "subtotal": float(
                            product.price * quantity
                        )

                    }


                    cart.append(item)

                    request.session["cart"] = cart


                    return redirect("create_sale")



        # Remove item from cart
        elif action == "remove":

            remove_id = int(
                request.POST.get("remove_id")
            )


            if 0 <= remove_id < len(cart):

                cart.pop(remove_id)



            request.session["cart"] = cart


            return redirect("create_sale")



        # Complete sale
        elif action == "complete":


            for item in cart:


                product = Product.objects.get(
                    id=item["id"]
                )


                # check stock again

                if product.stock < item["quantity"]:

                    error = (
                        f"Not enough stock for {product.name}"
                    )

                    break



                Sale.objects.create(

                    product=product,

                    quantity=item["quantity"]

                )


                product.stock -= item["quantity"]

                product.save()



            else:

                # only clear cart if all items saved

                request.session["cart"] = []


                return redirect("create_sale")



    else:

        form = SaleForm()



    total = sum(
        item["subtotal"]
        for item in cart
    )



    return render(
        request,
        "sale/create_sale.html",
        {
            "form": form,
            "cart": cart,
            "total": total,
            "error": error,
        }
    )