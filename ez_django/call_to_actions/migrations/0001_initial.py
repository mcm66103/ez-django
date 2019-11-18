# Generated by Django 2.2.7 on 2019-11-18 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CTA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=512)),
                ('cta', models.TextField(max_length=64)),
                ('cta_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogEmbeddedCTA',
            fields=[
                ('cta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='call_to_actions.CTA')),
            ],
            bases=('call_to_actions.cta',),
        ),
        migrations.CreateModel(
            name='HeaderCTA',
            fields=[
                ('cta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='call_to_actions.CTA')),
            ],
            bases=('call_to_actions.cta',),
        ),
    ]
