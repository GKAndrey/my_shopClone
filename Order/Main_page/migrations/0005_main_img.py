# Generated by Django 4.2.5 on 2023-12-04 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_page', '0004_alter_main_image_path_alter_main_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
