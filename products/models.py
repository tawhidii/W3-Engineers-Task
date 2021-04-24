from django.db import models

class Product(models.Model):
    """ Product model for products app"""

    title = models.CharField(max_length=200,db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)


    def __str__(self):
        return self.title



