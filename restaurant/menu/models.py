from django.db import models
from table_sessions.models import Tables

class Food(models.Model):
    food_name = models.CharField(max_length=100, unique=True, verbose_name="food name")
    description_of_food = models.TextField(max_length=500, verbose_name="description of food")
    price = models.IntegerField(default=50)
    def __str__(self):
        return self.food_name

class Drink(models.Model):
    drink_name =  models.CharField(max_length=100, unique=True, verbose_name="drink name")
    description_of_drink =  models.TextField(max_length=500, verbose_name="description of drink")
    price = models.IntegerField(default=20)
    def __str__(self):
        return self.drink_name
class Salad(models.Model):
    salad_name = models.CharField(max_length=100, unique=True, verbose_name="salad name")
    description_of_salad = models.TextField(max_length=500, verbose_name="description of salad")
    price = models.IntegerField(default=15)
    def __str__(self):
        return self.salad_name
class Desert(models.Model):
    desert_name =  models.CharField(max_length=100, unique=True, verbose_name="desert name")
    description_of_desert = models.TextField(max_length=500, verbose_name="description of desert")
    price = models.IntegerField(default=30)
    def __str__(self):
        return self.desert_name
    
class Order(models.Model):
    table_number = models.ForeignKey(Tables, on_delete=models.PROTECT)
    food = models.CharField(max_length=100)
    drink =models.CharField(max_length=100)
    salad =models.CharField(max_length=100)
    desert=models.CharField(max_length=100)
    total_price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.food}    {self.drink}    {self.salad}    {self.desert}   {self.total_price}"