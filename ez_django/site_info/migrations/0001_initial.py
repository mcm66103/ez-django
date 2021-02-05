# Generated by Django 2.2.13 on 2021-02-05 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('phone_number', models.TextField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
                ('keywords', models.TextField(max_length=256)),
                ('logo', models.ImageField(upload_to='site_info/')),
                ('favicon', models.ImageField(upload_to='site_info/')),
                ('facebook_url', models.CharField(max_length=512)),
                ('instagram_url', models.CharField(max_length=512)),
                ('twitter_url', models.CharField(max_length=512)),
                ('linkedin_url', models.CharField(max_length=512)),
                ('address', models.CharField(max_length=512)),
                ('blog_description', models.CharField(max_length=256)),
                ('blog_name', models.CharField(max_length=256)),
                ('blog_image', models.ImageField(upload_to='site_info/')),
                ('fb_app_id', models.CharField(max_length=255)),
            ],
        ),
    ]
