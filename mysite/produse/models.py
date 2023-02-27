from email.policy import default
from itertools import product
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Products(models.Model):
    product = models.CharField(max_length=100)
    cumparat = models.BooleanField(default=False)


    def __str__(self):
        return self.product + "-->" + str(self.cumparat)