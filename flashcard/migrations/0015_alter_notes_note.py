# Generated by Django 4.2.2 on 2023-06-16 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0014_notes_creator_subject_creator_topics_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='note',
            field=models.TextField(max_length=3000),
        ),
    ]
