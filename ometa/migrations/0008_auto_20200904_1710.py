# Generated by Django 3.1 on 2020-09-04 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ometa', '0007_auto_20200904_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='photograph',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='photograph', to='ometa.photographer'),
        ),
    ]
