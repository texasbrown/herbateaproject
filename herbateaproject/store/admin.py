from django.contrib import admin
from .models import ContactUs, Customer, Orders


# Register your models here.
admin.site.register(Customer)
admin.site.register(ContactUs)
admin.site.register(Orders)


#@admin.register(Orders)
#class OrdersAdmin(admin.ModelAdmin):
 #  list_display = ('orderID', 'order_date', 'customerID','email', 'productID.product_name', 'total_price')
  # ordering = ('-orderID',)
   #search_fields = ('orderID', 'customerID.fname', 'email', 'total_price')


#@admin.register(ContactUs)
#class ContactUsAdmin(admin.ModelAdmin):
#   list_display = (('full_name', 'email'), 'description')
#   ordering = ('-iD',)
#   search_fields = ('iD', 'email')
