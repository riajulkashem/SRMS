from django.db import models
from subjects.models import StudentClass
from students.models import Student
from django.urls import reverse
from django.contrib.postgres.fields import JSONField

# Create your models here.

class DeclareResult(models.Model):
    select_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    select_student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks = JSONField(blank=True)

    def get_absolute_url(self):
        return reverse('results:declare_result')
    def __str__(self):
        return "%s Section-%s" % (self.select_class.class_name, self.select_class.section)
