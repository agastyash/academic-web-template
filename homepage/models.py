#import datetime

from django.db import models
#from django.utils import timezone
#from django.contrib import admin

class Testimonial(models.Model):
    author = models.CharField(help_text="Testimonial Author", max_length=100)
    text = models.TextField(help_text="Testimonial Contents")
    def __str__(self):
        return self.author

class Course(models.Model):
    title = models.CharField(help_text="Course Title/Name", max_length=100)
    description = models.TextField(help_text="Course Description")
    target = models.CharField(default="Everyone", help_text="Who is the course for? eg. Year X/Year X to Y/Year X+/NAPLAN/JEE", max_length=100)

    def __str__(self):
        return self.title

class Result(models.Model):
    caption = models.CharField(help_text="Result Caption", max_length=100)
    image = models.ImageField(help_text="Result Image, 1:1 square only")
    def __str__(self):
        return self.caption
    
class Teacher(models.Model):
    name = models.CharField(help_text="Teacher's Name", max_length=100)
    # disabled indev feature because it's almost completely useless lmao
    # position = models.TextField(help_text="Optional caption", blank=True, default="")
    image = models.ImageField(help_text="Profile Image, 1:1 only")
    def __str__(self):
        return self.name