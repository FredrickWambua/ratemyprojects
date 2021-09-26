# Generated by Django 3.2.7 on 2021-09-25 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0005_project_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='location',
            field=models.CharField(max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='posted_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
