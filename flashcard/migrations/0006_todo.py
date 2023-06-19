# Generated by Django 4.2.2 on 2023-06-14 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0005_friendship'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_accomplished', models.BooleanField(default=False)),
                ('accomplished', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
