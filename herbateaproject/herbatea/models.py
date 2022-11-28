from django.db import models


class ContactUs(models.Model): 
   iD = models.IntegerField(primary_key = True)
   full_name = models.CharField(max_length = 50)
   email = models.EmailField(blank = False, null = False)
   mobile_number = models.CharField(max_length = 20, blank = True)
   description = models.CharField(max_length = 500)


   def __str__(self):
      return self.full_name + '' + self.email
