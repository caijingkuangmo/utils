from django.db import models

# Create your models here.

class ClassList(models.Model):
    cid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=32)

class Teacher(models.Model):
    tid = models.AutoField(primary_key=True)
    tname = models.CharField(max_length=32)

class Student(models.Model):
    sid = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=32)
    gender_choice = (
        (0,"男"),
        (1,"女"),
    )
    gender = models.SmallIntegerField(choices=gender_choice)
    class_obj = models.ForeignKey(to="ClassList", on_delete=models.CASCADE)

class Course(models.Model):
    cid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=32)
    teacher = models.ForeignKey(to="Teacher", on_delete=models.CASCADE)

class Score(models.Model):
    sid = models.AutoField(primary_key=True)
    student = models.ForeignKey(to="Student", on_delete=models.CASCADE)
    course = models.ForeignKey(to="Course", on_delete=models.CASCADE)
    number = models.IntegerField()

