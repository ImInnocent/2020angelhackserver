from django.db import models

# Create your models here.
class Message(models.Model):
    dday = models.IntegerField(default=0)
    text = models.CharField(max_length=400)

    # def __str__(self):
    #     return f"D-{dday}: {text}"