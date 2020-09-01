from django.db import models

class djangoClasses(models.Model):
    title = models.CharField(max_length=50),
    course_number = models.IntegerField(max_length=20),
    instructor_name = models.CharField(max_length=30)
    duration = models.FloatField()

    course = models.Manager()

obj1=djangoClasses()
obj1.title = "Migrations"
obj1.course_number = 101
obj1.instructor_name = "Brown"
obj1.duration=1.5

obj2=djangoClasses()
obj2.title = "PyCharm"
obj2.course_number = 120
obj2.instructor_name = "Smith"
obj2.duration=1.0

obj3=djangoClasses()
obj3.title = "Scripts"
obj3.course_number = 150
obj3.instructor_name = "Goldstein"
obj3.duration=2.0