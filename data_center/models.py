from django.db import models

class Course(models.Model):
    """Course database schema"""
    no = models.CharField(max_length=20, blank=True)
    code = models.CharField(max_length=20, blank=True)
    eng_title = models.CharField(max_length=80, blank=True)
    chi_title = models.CharField(max_length=80, blank=True)
    note = models.CharField(max_length=80, blank=True)
    object = models.CharField(max_length=20, blank=True)
    time = models.CharField(max_length=20, blank=True)
    teacher = models.CharField(max_length=40, blank=True) # Only save Chinese
    room = models.CharField(max_length=20, blank=True)
    credit = models.IntegerField(blank=True)
    limit = models.IntegerField(blank=True)
    prerequisite = models.BooleanField(default=False, blank=True)

    syllabus = models.TextField(blank=True) # A html div

    def __str__(self):
        return self.no