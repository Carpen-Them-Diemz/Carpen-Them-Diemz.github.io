# Generated by Django 4.2.1 on 2023-05-25 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_aiproject_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='aiproject',
            name='project_type',
            field=models.CharField(default='Machine Learning', max_length=30),
        ),
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.CharField(default='Web Development', max_length=50),
        ),
    ]
