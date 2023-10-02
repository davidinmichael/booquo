from django.db import models

class Books(models.Model):
    name = models.CharField(max_length=70)
    price = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    instock = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} | {self.price}"
    