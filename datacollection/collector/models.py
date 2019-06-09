from django.db import models

# Create your models here.


class Family(models.Model):
    folder_number = models.CharField(max_length=255)
    address = models.TextField(blank=True)

    def __str__(self):
        return str(self.folder_number) if self.folder_number else ''


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

    MARITAL_STATUS = (('married', 'married'), ('unmarried', 'unmarried'),('unkown','unknown'))
    GENDER_VALUES = (('male', 'male'), ('female', 'female'), ('other', 'other'))

    member_name = models.CharField(max_length=255, blank=True)
    age = models.IntegerField(blank=True)git
    gender = models.CharField(choices=GENDER_VALUES, max_length=255, default='female')
    relationship_to_head_of_family = models.CharField(
        choices=HUMAN_RELATIONSHIPS, max_length=255, default='head'
    )
    education = models.CharField(max_length=255,blank=True )
    occupation = models.CharField(max_length=255, blank=True)
    income = models.IntegerField(blank= True, null=True)
    marital_status = models.CharField(max_length=255, choices = MARITAL_STATUS, blank = True)
    immunization = models.TextField(max_length=255, blank =True)
    remarks = models.TextField(blank = True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.member_name) if self.member_name else ''


class MedicalRecord(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    clinical_details = models.TextField()
    diagnosis = models.TextField(blank=True)
    date = models.DateField()

    def __str__(self):
        return self.member.member_name if self.member else ''
