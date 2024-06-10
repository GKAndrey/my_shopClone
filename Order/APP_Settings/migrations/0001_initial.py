# Generated by Django 4.2.4 on 2023-11-06 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.JSONField(blank=True, null=True)),
                ('price', models.IntegerField()),
                ('img_path', models.URLField(blank=True, null=True)),
            ],
        ),
    ]