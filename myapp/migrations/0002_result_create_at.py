# Generated by Django 4.0.2 on 2022-02-23 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=True),
            preserve_default=False,
        ),
    ]