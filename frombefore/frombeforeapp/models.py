from django.db import models
from datetime import datetime

# Create your models here.
class Message(models.Model):
    dday = models.IntegerField(default=0)
    text = models.CharField(max_length=400)
    subject = models.CharField(max_length=40, default='college')
    edit_date = models.DateTimeField(default=datetime.now)

    # def __str__(self):
    #     return f"D-{dday}: {text}"
    def as_dict(self):
        return {
            "dday": self.dday,
            "text": self.text,
            "subject": self.subject,
            "edit_date": self.edit_date.strftime('%Y-%m-%d'),
        }

class UserData(models.Model):
    uuid = models.CharField(max_length=40)
    subject = models.CharField(max_length=40, default='college')
    
    def as_dict(self):
        return {
            "uuid": self.uuid,
            "subject": self.subject,
        }