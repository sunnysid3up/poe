from django.core.validators import validate_comma_separated_integer_list
from django.db import models
from content.choices import AscendancySkillTypes


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


class PassiveSkillModel(models.Model):
    class Meta:
        db_table = "passive_skill"

    name = models.CharField(max_length=45)
    ascendancy = models.ForeignKey(
        AscendancyModel, related_name="passive_skill", on_delete=models.CASCADE
    )
    skill_type = models.CharField(max_length=5, choices=AscendancySkillTypes.choices)
    stats = models.TextField(validators=[validate_comma_separated_integer_list])
