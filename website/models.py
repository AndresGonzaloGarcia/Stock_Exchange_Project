from django.db import models

class Stocks(models.Model):
    stock_code = models.CharField(max_length= 5)
    price= models.DecimalField(max_digits= 10, decimal_places= 2)
    
class TickerCode(models.Model):
    title = models.CharField(max_length= 40)
    ticker = models.CharField(max_length= 5)