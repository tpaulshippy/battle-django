from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=200)
    hp = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.hp})"