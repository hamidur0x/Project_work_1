from django.db import models, transaction
from inventory.models import Product


class Sale(models.Model):
    sold_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return sum(item.subtotal for item in self.items.all())


class SaleItem(models.Model):
    sale = models.ForeignKey(
        Sale,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT
    )

    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    @property
    def subtotal(self):
        return self.quantity * self.product.price


    def save(self, *args, **kwargs):

        with transaction.atomic():

            if self._state.adding:

                product = Product.objects.select_for_update().get(
                    id=self.product.id
                )

                if product.stock < self.quantity:
                    raise ValueError(
                        f"Not enough stock for {product.name}. Available stock: {product.stock}"
                    )

                product.stock -= self.quantity
                product.save(update_fields=["stock"])

                self.product = product

        super().save(*args, **kwargs)