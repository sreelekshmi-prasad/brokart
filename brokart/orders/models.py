from django.db import models
from customers.models import Customer

# Create your models here.

class Cart(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICE=((LIVE,'Live'),(DELETE,'Delete'))
    
    owners=models.ForeignKey(customer,on_delete=models.SET_NULL,related_name='orders')
    delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
   
   
   class CartItem (models.Model):
     product=models.ForeignKey(product,related_name='added_carts',on_delete=models.SET_NULL)
     quantity=models.IntegerField(default=1)


