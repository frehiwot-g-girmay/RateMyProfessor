# Generated by Django 2.1.4 on 2018-12-29 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webview', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('credits', models.IntegerField()),
            ],
        ),
    ]
