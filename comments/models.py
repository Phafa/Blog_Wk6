from django.db import models

# Create your models here.
class comment(models, Model):
    content = models.textfield()
    createdtime = models.DatetimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)