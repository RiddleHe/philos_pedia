# Generated by Django 4.1.3 on 2022-11-16 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('topic', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='pedia.topic')),
            ],
        ),
    ]
