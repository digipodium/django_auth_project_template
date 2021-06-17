from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField
from django.contrib.auth.models import User

# Create your models here.
class PurchaseModel(models.Model):
    """Model definition for PurchaseModel."""
    buyer = models.ForeignKey(User,on_delete=CASCADE)
    name = CharField(max_length=30)
    qty = IntegerField(verbose_name="Quantity")
    total_amt = IntegerField(verbose_name="total amount")

    class Meta:
        """Meta definition for PurchaseModel."""

        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'

    def __str__(self):
        return f"{self.name} {self.qty}"

class Product(models.Model):
    
    name = models.CharField(max_length=255) 
    image = models.ImageField(upload_to='products/') 
    price = models.FloatField()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
