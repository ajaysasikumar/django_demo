from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class StudentInfo(models.Model):
    student_id=models.CharField(max_length=10,null=True)
    name=models.CharField(max_length=250)
    Class=models.CharField(max_length=3)
    Place=models.CharField(max_length=300)
    phone=models.BigIntegerField()
    user=models.OneToOneField(User,models.CASCADE,related_name='Student_profile',default=None)


class Academics(models.Model):
    student_id=models.ForeignKey(StudentInfo,on_delete=models.CASCADE)    
    maths=models.IntegerField()
    physics=models.IntegerField()
    chemistry=models.IntegerField()
    computer_science=models.IntegerField()
    english=models.IntegerField()



