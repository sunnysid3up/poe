from django.db import models


class PoeClassModel(models.Model):
    name = models.CharField(max_length=10)
    announced_date = models.DateField()
    core_attribute = models.CharField(max_length=10)
    combat_focus = models.CharField(max_length=50)