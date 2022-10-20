from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_id = models.CharField(max_length=9)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"


class Grade(models.Model):
    level = models.CharField(max_length=10)

    def __str__(self):
        return self.level


class Movie(models.Model):
    name = models.CharField(max_length=100)
    poster_url = models.URLField(max_length=200)
    duration = models.DurationField()
    grade = models.ForeignKey(Grade, null=True, on_delete=models.SET_NULL)
    release_date = models.DateField()
    # genre = models.CharField(max_length=50, blank=True, null=True)
    # gv_id = models.CharField(max_length=10, blank=True, null=True)
    purchase_url = models.CharField(max_length=200, blank=True, null=True)
    star = models.BooleanField()
    def __str__(self):
        return self.name
