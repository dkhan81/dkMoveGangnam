# Generated by Django 2.0.4 on 2018-05-11 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='emp_period',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
