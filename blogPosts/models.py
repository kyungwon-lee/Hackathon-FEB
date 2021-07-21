from django.db import models
from django.utils import timezone

    


class Post(models.Model): 
    
    section = models.CharField(max_length=256, null=True)
    sub_section = models.CharField(max_length=256, null=True)
    title = models.CharField(max_length=256)
    brief_description = models.CharField(max_length=256, null=True)
    image = models.ImageField(upload_to='feed_image', blank = True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    # author = models.ForeignKey(User, null=True, on_delete = models.CASCADE)
    #like_users = models.ManyToManyField(User,blank=True, related_name='like_feeds',through='Like')

    #likes = models.ManyToManyField(User, related_name='blog_Posts')

    def __str__(self):
        return self.title



class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)


    def update_date(self): 
        self.updated_at = timezone.now()
        self.save()

    


