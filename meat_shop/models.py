from django.db import models
from restauth.models import EmailAccount


class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='static', blank=True, null=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Favorite(models.Model):
    user = models.ForeignKey(EmailAccount, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product}'



class Profile(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    user = models.ForeignKey(EmailAccount, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=20,default='baghdad')

    def __str__(self):
        return f'{self.name} - {self.phone_number}'



class Cart(models.Model):
    user = models.ForeignKey(EmailAccount, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.product}'



class Order(models.Model):
    user = models.ForeignKey(EmailAccount, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product}'