# Generated by Django 4.1.3 on 2023-02-12 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childmissingapp', '0003_complainant_history_user_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_history',
            name='staus',
            field=models.CharField(max_length=50),
        ),
    ]