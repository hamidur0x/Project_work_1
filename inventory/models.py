from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50, choices=[('Rice', 'Rice'), ('Sope', 'Sope'), ('Milk', 'Milk'),('Onions','Onions'), ('Garlic','Garlic'),('Potatoes','Potatoes'),('Peppers','Peppers'),('Bananas','Bananas'),('Apples','Apples'),('Oil','Oil')])
    stock = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, choices=[('Frozen Foods',  'Frozen Foods'),('Meat', 'Meat'), ('Bakery','Bakery'),('Household', 'Household'), ('Dry Goods', 'Dry Goods'), ('Clothing', 'Clothing'), ('Snacks', 'Snacks')])
    unit = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50, choices=[('kg', 'kg'), ('liter', 'liter'), ('piece', 'piece')])

    def __str__(self):
        return self.name