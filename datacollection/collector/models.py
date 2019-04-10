from django.db import models

# Create your models here.


class Family(models.Model):
    folder_number = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return str(self.folder_number)


class Member(models.Model):
    HUMAN_RELATIONSHIPS = (
        ('head', 'head'),
        ('father', 'father'),
        ('mother','mother'),
        ('daughter','daughter'),
        ('child','child'),
        ('brother', 'brother'),
        ('sister', 'sister'),
        ('grandfather', 'grandfather'),
        ('uncle', 'uncle'),
        ('aunt', 'aunt'),
        ('father in law', 'father in law'),
        ('mother in law', 'mother in law'),
        ('son in law', 'son in law'),
        ('daughter in law', 'daughter in law'),
        ('brother in law', 'sister in law'),
        ('husband', 'husband'),
        ('wife', 'wife'),
        ('unknown', 'unknown')
    )

    MARITAL_STATUS = (('married', 'married'), ('unmarried', 'unmarried'),)
    GENDER_VALUES = (('male', 'male'), ('female', 'female'))

    name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True)
    gender = models.CharField(choices=GENDER_VALUES, max_length=255, default='female')
    relationship_to_head_of_family = models.CharField(
        choices=HUMAN_RELATIONSHIPS, max_length=255, default='head'
    )
    education = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    income = models.IntegerField()
    marital_status = models.CharField(max_length=255, choices = MARITAL_STATUS)
    immunization = models.TextField(max_length=255)
    remarks = models.TextField()
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MedicalRecord(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    clinical_details = models.TextField()
    diagnosis = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.member
