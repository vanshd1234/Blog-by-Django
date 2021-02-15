# Generated by Django 3.1.5 on 2021-02-07 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('post', models.CharField(default='', max_length=500)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
    ]
