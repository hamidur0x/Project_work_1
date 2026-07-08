from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    stock = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, choices=[('Frozen Foods',  'Frozen Foods'),('Meat', 'Meat'), ('Bakery','Bakery'),('Household', 'Household'), ('Dry Goods', 'Dry Goods'), ('Clothing', 'Clothing'), ('Snacks', 'Snacks')])
    unit = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50, choices=[('kg', 'kg'), ('liter', 'liter'), ('piece', 'piece')])

    def __str__(self):
        return self.name