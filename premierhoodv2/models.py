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


class Stock_Influence(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_price = models.IntegerField()


class Stock_Creativity(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_price = models.IntegerField()


class Stock_Impact(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_price = models.IntegerField()
