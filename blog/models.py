from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published")


class Post(models.Model):
    """
    sets the table headers for Post
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

class Meta:
    """
    sets the order in which the blog posts are displayed
    """
    ordering = ["-created_on"]

def __str__(self):
    """
    makes the new items in the database display under the title name
    this returns string repersentation of an object
    """
    return self.title

def number_of_likes(self):
    """
    returns the total number of likes on a post
    """
    return self.likes.count()

class Comment(models.Model):
    """
    sets the table for comments
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

class Meta:
    """
    ascending order, the olders are listed first
    """
    ordering = ["created_on"]

def __str__(self):
    return f"Comment {self.body} by {self.name}"
