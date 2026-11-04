from django.db import models

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=20)
    description=models.TextField()
    duration=models.CharField(max_length=20)
    fee=models.IntegerField()
    level=models.CharField(max_length=10)

    image=models.ImageField(upload_to='media',null=True)