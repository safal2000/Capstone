from django.db import models

class Product(models.Model):
    """
    This product model is the model used for the app, it defines the content rules of the app.

    Rules:
        Certain rules that the product model applies is the max length of the title of a product
        being 200 characters.

        The price of the product having a max digit of 10 with 2 decimal paces/

        Only being able to show positive integers for the quantity of a product
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title

