# Generated by Django 4.1.3 on 2023-02-11 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childmissingapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='police',
            name='badge_number',
            field=models.CharField(default='00000', max_length=10),
        ),
    ]
