from django.db.models import TextChoices


class AscendancySkillTypes(TextChoices):
    """ Ascendancy passive skill types"""

    MINOR_SKILLS = "MINOR"
    MAJOR_SKILLS = "MAJOR"
