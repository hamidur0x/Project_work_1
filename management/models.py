from django.db import models
from django.db import transaction
from inventory.models import Product

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    sold_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return self.quantity * self.product.price
    def save(self, *args, **kwargs):
        with transaction.atomic():
            if self._state.adding:  # only on creation
                p = Product.objects.select_for_update().get(pk=self.product.pk)
                if p.stock < self.quantity:
                    raise ValueError("Insufficient stock")
                p.stock -= self.quantity
                p.save(update_fields=["stock"])
            super().save(*args, **kwargs)


