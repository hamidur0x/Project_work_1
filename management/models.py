from django.db import models
from inventory.models import Product


class Sale(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField()

    date = models.DateTimeField(
        auto_now_add=True
    )


    @property
    def subtotal(self):
        return self.quantity * self.product.price