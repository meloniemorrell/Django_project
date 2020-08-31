from django.db import models

class djangoClasses(models.Model):
    title = models.CharField(max_length=50),
    course_number = models.IntegerField(max_length=20),
    instructor_name = models.CharField(max_length=30)
    duration = models.Float(max_length=20)

    course = models.Manager()

    def __init__(self, title, course_number, instructor_name, duration):
        self.title = 'Database storage',  'Writing a field', 'Database storage'
        self.course_number = 100, 200, 300
        self.instructor_name = 'Jones', 'Brown', 'Thomas'
        self.duration = 1.5, 2.0, 1.0
