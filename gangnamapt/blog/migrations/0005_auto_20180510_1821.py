# Generated by Django 2.0.4 on 2018-05-10 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180510_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tech',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=10000),
        ),
    ]
