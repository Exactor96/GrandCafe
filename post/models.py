from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount, HitCountMixin
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30, db_index= True)
    def __str__(self):
        return '{}'.format(self.name)

class SubCategory(models.Model):
    name = models.CharField(max_length=30, db_index= True)
    category=models.ForeignKey(Category, on_delete = models.PROTECT,default=0)
    def __str__(self):
        return '{}'.format(self.name)

class Post(models.Model,HitCountMixin):
    title = models.CharField(max_length=150, db_index= True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    category = models.TextField(max_length=50, blank=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    ingredients = models.TextField(blank=False)
    cooking = models.TextField(blank=False)
    date_pub = models.DateTimeField(auto_now_add=True)
    time_cooking = models.TextField(blank=True, max_length=10)
    category = models.ForeignKey(Category, on_delete = models.PROTECT,default=0)
    subcategory=models.ForeignKey(SubCategory, on_delete = models.PROTECT,default=0)
    views = models.IntegerField(blank=False,default=0)
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')


    def ingredients_as_list(self):
        return self.ingredients.split('\n')

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ['-date_pub']

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return '{}'.format(self.title)


class Human(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    surname = models.CharField(max_length=50, verbose_name="Фамилия")
    date_birth = models.DateField(auto_now_add=False, auto_now=False, verbose_name='дата рождения')
    email = models.EmailField(max_length=50, verbose_name='email')

    def __str__(self):
        return self.name

class t_img(models.Model):
    avatar = models.ImageField(verbose_name="avatar")

    def __str__(self):
        return self.name
