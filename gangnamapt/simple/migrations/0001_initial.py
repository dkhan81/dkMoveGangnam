# Generated by Django 2.0.4 on 2018-05-02 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DkNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('text', models.TextField()),
                ('published_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
