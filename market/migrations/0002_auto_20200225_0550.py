# Generated by Django 3.0.3 on 2020-02-25 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='listing',
            name='critter_img',
            field=models.ImageField(default='poo', upload_to=''),
            preserve_default=False,
        ),
    ]
