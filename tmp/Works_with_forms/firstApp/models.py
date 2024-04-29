from django.db import models

# Create your models here.
# class Student(models.Model):
#     Name = models.CharField(max_length=20)
#     roll = models.IntegerField(primary_key=True)
#     address = models.TextField(default='Noakhali')
#     Father_Name = models.TextField(default='Alamgir')
    
#     def __str__(self):
#         return f"roll : {self.roll} , {self.Name}"


class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    father = models.CharField(max_length=20)
    address = models.TextField()
    
    def __str__(self):
        return f"Name : {self.name} "
