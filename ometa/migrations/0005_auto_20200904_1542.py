# Generated by Django 3.1 on 2020-09-04 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ometa', '0004_show_showphoto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={},
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(default='', upload_to='photo/'),
        ),
        migrations.AlterField(
            model_name='showphoto',
            name='photo',
            field=models.ImageField(default='', upload_to='photo/'),
        ),
    ]
