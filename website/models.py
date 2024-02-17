from django.db import models

class Stocks(models.Model):
    title= models.CharField(max_length= 50)
    stock_code = models.CharField(max_lenght= 5)
    price= models.DecimalField(decimal_places= 2)