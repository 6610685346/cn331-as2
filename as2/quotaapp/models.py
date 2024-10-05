from email.policy import default
from enum import unique
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Subject(models.Model):
    subject_id = models.CharField(max_length=64, primary_key=True)
    subject_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.subject_id} {self.subject_name}"


class Course(models.Model):
    course = models.ForeignKey(Subject, on_delete=models.CASCADE)
    semester = models.CharField(max_length=64)
    year = models.CharField(max_length=64)
    seat = models.PositiveIntegerField(default=0)
    current_seat = models.PositiveIntegerField(default=0)
    q_status = models.CharField(max_length=64, choices=[(
        'Available', 'Available'), ('Full', 'Full')], default="Available")
    status = models.BooleanField(default=True)

    class Meta:
        unique_together = ['course', 'semester', 'year']

    def __str__(self):
        return f"{self.course.subject_id} {self.semester} {self.year}"

    def is_seat_available(self):
        return self.student_apply.count() < self.seat


class Student(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    applys = models.ManyToManyField(
        Course, blank=True, related_name="student_apply")

    def __str__(self):
        return f"{self.student} {self.student.first_name} {self.student.last_name}"
