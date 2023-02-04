from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username



class Rack(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, null=True, blank=True)
    part_no = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.city.name} - {self.location}"


class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    sequence = models.IntegerField(blank=True, null=True)
    variant = models.CharField(max_length=15, blank=True, null=True)
    variant_code = models.CharField(max_length=15, blank=True, null=True)


    def __str__(self):
        return self.name


class Part(models.Model):
    part_no = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    mrp = models.FloatField()
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    rack = models.ForeignKey('Rack', on_delete=models.CASCADE)
    vehicle = models.ManyToManyField(Vehicle, related_name='eligible_models', blank=True)
    barcode = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return self.part_no


class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name=models.CharField(max_length=50)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=20)
    order_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    order_status = models.CharField(max_length=50)
    order_total = models.FloatField()
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.order_id