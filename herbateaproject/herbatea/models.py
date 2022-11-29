from django.db import models



class ContactUs(models.Model): 
   iD = models.IntegerField(primary_key = True)
   full_name = models.CharField(max_length = 50)
   email = models.EmailField(blank = False, null = False)
   mobile_number = models.CharField(max_length = 20, blank = True)
   description = models.CharField(max_length = 500)


   def __str__(self):
      return self.full_name + '' + self.email


class Customer(models.Model):
   customerid = models.IntegerField(primary_key=True, default='1', blank=True)
   fname = models.CharField(max_length=50, null = True)
   lname = models.CharField(max_length=100, null = True)
   email = models.EmailField(max_length=200, null = True)
   password = models.CharField(max_length=50, null = True)

   def __str__(self):
      return self.fname + ' ' + self.lname


class Products(models.Model):
   pass

class Orders(models.Model):
   customerID = models.ForeignKey(Customer, null = True, on_delete=models.PROTECT)
   orderID = models.CharField(primary_key = True, max_length = 50)
   productID = models.ForeignKey('Products', on_delete=models.PROTECT)
   email = models.EmailField(null = True)
   delivery_address = models.CharField(max_length = 300, null = True)
   total_price = models.FloatField(null = True)
   # Many users can make many orders.
   #orders = models.ManyToMany('Self', Customer, blank = True, on_delete=models.PROTECT)
   order_date = models.DateTimeField(auto_now = True, null = True)
   order_status = models.CharField(max_length = 10, null = True)

   # change 'self.customerID' to field in table to show the name of the customer and for "ProductID" to shoew the product name

#def __str__(self):
#     return self.orderID + '' + self.order_date + '' + self.customerID.fname + '' + self.email
