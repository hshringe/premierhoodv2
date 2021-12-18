from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=256,  primary_key=True)
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=512)

class Player(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    buy_count = models.IntegerField(default=0)

class UserStocksOwned(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Player, on_delete=models.CASCADE)

class Stock_Influence(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE, primary_key=True)
    current_price = models.DecimalField(max_digits=30, decimal_places=15)

class Stock_Creativity(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE, primary_key=True)
    current_price = models.IntegerField()

class Stock_Impact(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE, primary_key=True)
    current_price = models.DecimalField(max_digits=30, decimal_places=15)
