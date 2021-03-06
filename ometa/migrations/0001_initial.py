# Generated by Django 3.1 on 2021-01-05 12:33

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_U',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('information', models.TextField(blank=True, null=True)),
                ('isVisible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Addres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='No email', max_length=30)),
                ('place', models.CharField(default='No address', max_length=120)),
                ('link_for_google_maps', models.CharField(default='No link', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='No name', max_length=30)),
                ('position', models.CharField(default='No position', max_length=30)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(default='No phone number', max_length=128, region=None)),
                ('email', models.EmailField(default='No email', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('name', models.CharField(default='No name', max_length=30)),
                ('preview', models.ImageField(blank=True, null=True, upload_to='directors_preview')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('name', models.CharField(default='No name', max_length=30)),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Preview_Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('name', models.CharField(default='No name', max_length=30)),
                ('nameSecond', models.CharField(max_length=30)),
                ('video', models.FileField(blank=True, null=True, upload_to='preview_video')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('name', models.CharField(max_length=120)),
                ('choice_player', models.CharField(choices=[('YouTube', 'YouTube'), ('vimeo', 'vimeo')], default='vimeo', max_length=7)),
                ('link_for_video', models.CharField(default='Video is not loaded', max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('name', models.CharField(default='No name', max_length=50)),
                ('choice_player', models.CharField(choices=[('YouTube', 'YouTube'), ('vimeo', 'vimeo')], default='vimeo', max_length=7)),
                ('link_for_video', models.CharField(default='Video is not loaded', max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('director', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='director', to='ometa.director')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('photo', models.ImageField(blank=True, default='', null=True, upload_to='photo/')),
                ('isTitle', models.BooleanField(default=0)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='ometa.album')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.AddField(
            model_name='album',
            name='photograph',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='photograph', to='ometa.photographer'),
        ),
    ]
