# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_instagram_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='instagram_post',
            name='search_term',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
