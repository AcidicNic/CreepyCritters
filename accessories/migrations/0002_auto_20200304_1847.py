# Generated by Django 3.0.3 on 2020-03-04 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accessories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
