from django.db import models


class CharacterModel(models.Model):
    class Meta:
        db_table = "character"

    name = models.CharField(max_length=20)
    announced_date = models.DateField()
    core_attribute = models.CharField(max_length=45)
    description = models.TextField()

    def __str__(self):
        return self.name


class AscendancyModel(models.Model):
    class Meta:
        db_table = "ascendancy"

    name = models.CharField(max_length=20)
    announced_date = models.DateField()
    character = models.ForeignKey(
        CharacterModel, related_name="ascendancy", on_delete=models.CASCADE
    )
    description = models.TextField()
