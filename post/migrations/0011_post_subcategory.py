# Generated by Django 2.2.2 on 2019-06-11 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_auto_20190611_0606'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subcategory',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='post.SubCategory'),
        ),
    ]