from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

STATUS = ((0, 'Draft'), (1, 'Published'))


class Enter(models.Model):

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
        ordering = ['-created_on']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Enter, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):

    post = models.ForeignKey(
        Enter, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'
