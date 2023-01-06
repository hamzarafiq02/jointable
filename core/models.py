from django.db import models

# Create your models here.
class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    roll_no = models.IntegerField()
    city = models.CharField(max_length=70)
    marks = models.IntegerField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True)
    pass_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']