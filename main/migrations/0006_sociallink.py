# Generated by Django 5.0.6 on 2024-07-07 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_suscriber_subscriber'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gitlink', models.TextField()),
                ('Linkedlink', models.TextField()),
                ('Discordlink', models.TextField()),
                ('Youtubelink', models.TextField()),
            ],
        ),
    ]
