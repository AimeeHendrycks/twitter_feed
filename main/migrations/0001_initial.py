# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=255, null=True, blank=True)),
                ('profile_image_url', models.CharField(max_length=255, null=True, blank=True)),
                ('screen_name', models.CharField(max_length=255, null=True, blank=True)),
                ('created_at', models.CharField(max_length=255, null=True, blank=True)),
                ('location', models.CharField(max_length=255, null=True, blank=True)),
                ('search_term', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
    ]
