from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Post)
admin.site.register(models.Tag)
admin.site.register(models.Profile)
#admin.site.register(models.t_img)
admin.site.register(models.Category)
admin.site.register(models.SubCategory)
