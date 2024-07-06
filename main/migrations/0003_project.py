# Generated by Django 5.0.6 on 2024-07-06 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('banner', models.ImageField(upload_to='banner')),
                ('intro', models.TextField()),
                ('discription', models.TextField()),
                ('iframe', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
