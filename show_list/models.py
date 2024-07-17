from django.db import models
from django.utils import timezone
from datetime import date
# Create your models here.
class do_list(models.Model):
    title = models.CharField(max_length = 20)
    description = models.CharField(max_length = 200)
    deadline = models.DateField(default = date.today)
    pub_time = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title