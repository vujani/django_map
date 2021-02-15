# Generated by Django 3.1.6 on 2021-02-15 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_testmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestModel',
        ),
        migrations.AlterField(
            model_name='unverifiedtag',
            name='x_coord',
            field=models.FloatField(verbose_name='Координата X'),
        ),
        migrations.AlterField(
            model_name='unverifiedtag',
            name='y_coord',
            field=models.FloatField(verbose_name='Координата Y'),
        ),
    ]
