# Generated by Django 4.1.1 on 2022-10-09 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0003_rename_name_author_first_name_author_last_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="genre",
        ),
        migrations.RemoveField(
            model_name="movie",
            name="gv_id",
        ),
    ]
