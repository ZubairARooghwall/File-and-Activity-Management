# Generated by Django 4.2.2 on 2023-06-22 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0035_alter_groupmessages_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
