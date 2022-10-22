from django.db import models

# Create your models here.
class Feature(models.Model):
    id : int
    name : str
    details : str
    is_true : bool