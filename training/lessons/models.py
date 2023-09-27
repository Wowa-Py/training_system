from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    accesses = models.ManyToManyField('UserAccess')

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    video_link = models.URLField()
    duration = models.IntegerField()
    viewers = models.ManyToManyField(User, through='UserAccess')

    def __str__(self):
        return self.name

class UserAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    view_time = models.DateTimeField(auto_now_add=True)
    is_viewed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.course.name}'