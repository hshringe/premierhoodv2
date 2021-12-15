from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=512)


class Player(models.Model):
    id = models.IntegerField()
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    position = models.CharField(max_length=256)


class Stock_Rating(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    price_at_purchase = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_price = models.IntegerField()
    purchase_date = models.DateTimeField()


class Stock_Creativity(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    price_at_purchase = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_price = models.IntegerField()
    purchase_date = models.DateTimeField()


class Stock_Impact(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    price_at_purchase = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_price = models.IntegerField()
    purchase_date = models.DateTimeField()
