# Generated by Django 2.2.6 on 2019-10-30 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighboor', '0018_auto_20191030_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighborhood',
            name='health_department_contact',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='neighborhood',
            name='police_authority_contact',
            field=models.IntegerField(),
        ),
    ]
