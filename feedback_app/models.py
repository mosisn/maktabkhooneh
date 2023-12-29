from django.db import models
from django.db.models import CharField
from course.models import Course

class Comments(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    name = models.CharField(max_length= 200)
    last_name = models.CharField(max_length= 200)
    email = models.EmailField()
    comment = models.TextField()
    
    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'
