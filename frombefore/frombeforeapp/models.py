from django.db import models
from datetime import datetime

# Create your models here.
class Message(models.Model):
    dday = models.IntegerField(default=0)
    text = models.CharField(max_length=400)
    edit_date = models.DateTimeField(default=datetime.now)

    # def __str__(self):
    #     return f"D-{dday}: {text}"
    def as_dict(self):
        return {
            "dday": self.dday,
            "text": self.text,
            "edit_date": self.edit_date.strftime('%Y-%m-%d'),
        }
