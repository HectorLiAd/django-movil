# Generated by Django 3.2.8 on 2021-10-10 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagen', '0002_alter_imagen_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagen',
            name='detail',
            field=models.TextField(blank=True, null=True),
        ),
    ]
