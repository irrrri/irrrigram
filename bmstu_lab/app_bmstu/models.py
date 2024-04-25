from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count, Sum
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(blank=True, upload_to="avatars/")

    def __str__(self):
        return f"id = {self.id}, {self.user.get_username()}"


class Post(models.Model):
    text = models.TextField()
    photo = models.ImageField(blank=True, upload_to="photos/")
    rating = models.IntegerField(default=0)
    statusChangeDate = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name="posts",
                              related_query_name="post")
    likes = models.ManyToManyField('Profile', through="LikePost", related_name="post_likes",
                                   related_query_name="post_like")

    def __str__(self):
        return f"id = {self.id}, {self.title}"


class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name="comments",
                                 related_query_name="comment")
    author = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name="comments",
                               related_query_name="comment")

    def __str__(self):
        return f"id = {self.id}, {self.text[0:5]}"


class LikePost(models.Model):
    user = models.ForeignKey('Profile', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "post"],
                name="unique_like_post",
            ),
        ]

    def __str__(self):
        return f"Who = {self.user.id}, what = {self.question.id}"