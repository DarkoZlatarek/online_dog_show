"""
Database models for the dogshow app
& comments section.
"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

STATUS = ((0, 'Draft'), (1, 'Published'))


# Model used from "I think therefore I blog" walkthrough.
class Enter(models.Model):
    """
    Database model for submitting an entry
    """
    title = models.CharField(
        max_length=200, unique=True, null=False, blank=False)
    slug = models.SlugField(
        max_length=200, unique=True, null=False, blank=False)
    competitor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post_enter')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    class Meta:
        """
        To display entries in descending order
        """
        ordering = ['-created_on']

    def save(self, *args, **kwargs):
        """
        Auto populate slug field
        """
        self.slug = slugify(self.title)
        super(Enter, self).save(*args, **kwargs)

    def __str__(self):
        """
        To return a string representation of an object
        """
        return self.title

    def number_of_likes(self):
        """
        Return total number of entry likes
        """
        return self.likes.count()


# Model used from "I think therefore I blog" walkthrough.
class Comment(models.Model):
    """
    Database model for creating a comment
    on an entry
    """
    post = models.ForeignKey(
        Enter, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Order comments in ascending order
        """
        ordering = ['created_on']

    def __str__(self):
        """
        Display the comment as the comment text,
        and comment author name
        """
        return f'Comment {self.body} by {self.name}'
