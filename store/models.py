from django.db import models
from django.urls import reverse
from text.settings import AUTH_USER_MODEL
from django.utils import timezone
# Create your models here.
"""
Products
-Nom(txt)
-Prix(float ou int)
-QTX en stock (int)
-Description (txt)
-img
"""

class Product(models.Model):
    name = models.CharField(max_length=128) 
    slug = models.SlugField(max_length=128)
    price =models.FloatField(default=0.0)
    stock= models.IntegerField(default=0)
    description=models.TextField(blank=True)
    thumbnail=models.ImageField(upload_to="Product", blank=True, null=True) 

    def __str__(self):
        return f"{self.name} ({self.stock})"    
    
    def get_absolute_url(self):
        return  reverse("product", kwargs={"slug": self.slug})
    
#Article (order)
"""

-Utilisateur
-QTX 
-Commandé ou non 

"""
class Order(models.Model):
    user= models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True,null=True)


    def __str__(self):
        return f"{self.product.name}({self.quantity})"
#Panier (Cart)
"""

-Utilisateur
-Articles
-Commandé ou non 
-Date de la commande
"""
class Cart (models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)

    def __str__(self):
        return self.user.username

    def delete(self, *args, **kwargs):
        for order in self.orders.all():
            order.ordered= True
            order.ordered_date = timezone.now()
            order.save()
        self.orders.clear()
        super().delete(*args, **kwargs)

class VotreModele(models.Model):
    image = models.ImageField(upload_to='images/')