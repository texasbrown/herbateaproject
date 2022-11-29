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
   customerid= models.IntegerField(primary_key = True)
   fname = models.CharField(max_length=50)
   lname = models.CharField(max_length=100)
   email = models.EmailField(max_length=200)
   password = models.CharField (max_length=50)

   def __str__(self):
      return self.fname + ' ' + self.lname


class Orders(models.Model):
   customerID = models.ForeignKey('Customer Account ID', on_delete=models.PROTECT)
   orderID = models.CharField(primary_key=True)
   productID = models.ForeignKey('Prouct List', on_delete=models.PROTECT)
   email = models.ForeignKey('Customer Email', on_delete=models.PROTECT)
   delivery_address = models.CharField('Customer Delivery Address')
   total_price = models.FloatField('Total Price of Combined orders')
   # Update the "number_of_orders" section to draw from users table.
   orders_placed = models.ManyToMany('Customers Table', on_delete=models.PROTECT)
   order_date = models.DateTimeField('Date and time order was placed')
   order_status = models.CharField('Status would either be "Placed" or "Declined"', max_length=10)

   # change 'self.customerID' to field in table to show the name of the customer and for "ProductID" to shoew the product name

   def __str__(self):
      return self.orderID + '' + self.order_date + '' + self.customerID + '' + self.email + '' + self.productID + '' + self.total_price
