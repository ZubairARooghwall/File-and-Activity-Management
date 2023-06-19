# Generated by Django 4.2.2 on 2023-06-15 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0010_user_prefers_dark_theme_alter_notes_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='prefers_dark_theme',
            field=models.BooleanField(default=False, help_text='Do you prefer dark theme?'),
        ),
    ]
