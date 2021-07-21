from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Post(models.Model): 
    
    section = models.CharField(max_length=256, null=True)
    title = models.CharField(max_length=256)
    brief_description = models.CharField(max_length=256, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    like_dislike = models.ManyToManyField(User, blank=True, related_name='like_posts', through='LikeOrDislike')

    def update_date(self): 
        self.updated_at = timezone.now()
        self.save()
    
    def get_total_like(self):
        return LikeOrDislike.objects.filter(post_id = self.id, like=True).count()

    def get_total_dislike(self):
        return LikeOrDislike.objects.filter(post_id = self.id, dislike=True).count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'[post : {self.post}] {self.content}'

class LikeOrDislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField(default=False) # 좋아요
    dislike = models.BooleanField(default=False) # 싫어요
    created_at = models.DateTimeField(default=timezone.now)