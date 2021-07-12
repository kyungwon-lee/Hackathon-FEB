from django.db import models
from django.utils import timezone



class Post(models.Model): 
    
    section = models.CharField(max_length=256, null=True)
    title = models.CharField(max_length=256)
    brief_description = models.CharField(max_length=256, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def update_date(self): 
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title


