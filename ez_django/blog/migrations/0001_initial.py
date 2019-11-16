# Generated by Django 2.2.7 on 2019-11-16 19:09

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('slug', models.CharField(max_length=256)),
                ('content', tinymce.models.HTMLField(verbose_name='Content')),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('D', 'Draft'), ('P', 'Published')], max_length=2)),
                ('description', models.TextField()),
                ('keywords', models.TextField()),
            ],
            options={
                'ordering': ('-published',),
            },
        ),
    ]