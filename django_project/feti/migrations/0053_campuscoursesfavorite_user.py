# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feti', '0052_auto_20161101_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='campuscoursesfavorite',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL)
        ),
    ]