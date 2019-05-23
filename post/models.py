from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150, db_index= True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    category = models.TextField(max_length=50, blank=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    ingredients = models.TextField(blank=False)
    cooking = models.TextField(blank=False)
    date_pub = models.DateTimeField(auto_now_add=True)
    time_cooking = models.TextField(blank=True, max_length=10)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ['-date_pub']

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return '{}'.format(self.title)
