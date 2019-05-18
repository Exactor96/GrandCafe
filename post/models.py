from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150, db_index= True)
    slug = models.SlugField(max_length=150, unique=True)
    ingredients = models.TextField(blank=False, db_index = True)
    cooking = models.TextField(blank=False, db_index = True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.title)

