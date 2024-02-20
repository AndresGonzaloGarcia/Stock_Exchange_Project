from django import forms
from django.db import models


class TickerForm(forms.Form):
    ticket = models.CharField(max_length= 5)