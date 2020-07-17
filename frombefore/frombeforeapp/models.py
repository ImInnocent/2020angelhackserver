from django.db import models

# Create your models here.
class Message(models.Model):
    dday = models.IntegerField(default=0)
    text = models.CharField(max_length=400)

    # def __str__(self):
    #     return f"D-{dday}: {text}"
    def as_dict(self):
        return {
            "dday": self.dday,
            "text": self.text,
            # other stuff
        }