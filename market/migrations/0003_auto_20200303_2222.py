# Generated by Django 3.0.3 on 2020-03-03 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_auto_20200225_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='age_format',
            field=models.CharField(choices=[('YR', 'Year(s) old'), ('MO', 'Months old')], default='YR', help_text='Year/Month', max_length=2),
        ),
        migrations.AddField(
            model_name='listing',
            name='age_num',
            field=models.IntegerField(blank=True, help_text='Critter Age', null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='title',
            field=models.CharField(default='', help_text='Listing Title', max_length=36),
        ),
        migrations.AlterField(
            model_name='listing',
            name='critter_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='listing',
            name='desc',
            field=models.TextField(blank=True, default='', help_text='Describe your critter!'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='name',
            field=models.CharField(help_text="Critter's Name", max_length=16),
        ),
        migrations.AlterField(
            model_name='listing',
            name='type',
            field=models.CharField(choices=[('???', '???'), ('cryptid', 'Cryptid'), ('reptile', 'Reptile'), ('amphibian', 'Amphibian'), ('insect', 'Insect'), ('spider', 'Spider')], default='???', help_text='Critter Type', max_length=12),
        ),
    ]
