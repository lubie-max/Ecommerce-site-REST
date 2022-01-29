from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from products.models import Product

#django signals
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


class Cart(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    total_items= models.IntegerField(default=0)
    total_price= models.FloatField(default=0)
    ordered= models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.user) + " " + str(self.total_price) + "  Total Items-" + str(self.total_items)

    

class CartItem(models.Model):
    product_name= models.ForeignKey(Product , on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart= models.ForeignKey(Cart, on_delete=models.CASCADE)
    price= models.FloatField(default=0)
    quantity = models.IntegerField(default=1)

    def __str__(self) -> str:
        return str(self.product_name )




@receiver(pre_save, sender=CartItem)
def my_handler(sender, **kwargs):
    # print(kwargs)
    cart_item= kwargs['instance']
    product= Product.objects.get(id= cart_item.product_name.id)
    cart_item.price = cart_item.quantity * float(product.product_price)
    cart = Cart.objects.get(id=cart_item.cart.id)
    cart.total_price =cart.total_price + cart_item.price
    cart.save()
    # cart.total_items = len(cart_item.product_name)
    

    
