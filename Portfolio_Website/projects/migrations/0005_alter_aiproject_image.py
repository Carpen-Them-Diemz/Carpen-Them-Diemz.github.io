# Generated by Django 4.2.1 on 2023-05-25 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_aiproject_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aiproject',
            name='image',
            field=models.FilePathField(path='/img/AI'),
        ),
    ]
