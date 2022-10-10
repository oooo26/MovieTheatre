# Generated by Django 4.1.1 on 2022-10-06 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="gv_url",
        ),
        migrations.AddField(
            model_name="movie",
            name="gv_id",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="movie",
            name="genre",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
