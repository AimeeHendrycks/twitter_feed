# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instagram_post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=255, null=True, blank=True)),
                ('profile_picture', models.CharField(max_length=255, null=True, blank=True)),
                ('text', models.CharField(max_length=255, null=True, blank=True)),
                ('location', models.CharField(max_length=255, null=True, blank=True)),
                ('link', models.CharField(max_length=255, null=True, blank=True)),
                ('post_image', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
    ]
