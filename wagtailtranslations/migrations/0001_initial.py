# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 09:32
from __future__ import unicode_literals

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0030_index_on_pagerevision_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=12, verbose_name='language code')),
                ('is_default', models.BooleanField(default=False, help_text='\n        Visitors with no language preference will see the site in this\n        language\n        ', verbose_name='is default language?')),
                ('order', models.IntegerField(help_text='\n        Language choices and translations will be displayed in this order\n        ', verbose_name='order')),
                ('live', models.BooleanField(default=True, help_text='Is this language available for visitors to view?', verbose_name='live')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='TranslatedPage',
            fields=[
                ('translated_page_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='+', serialize=False, to='wagtailcore.Page')),
                ('translation_key', models.UUIDField(db_index=True, default=uuid.uuid4, verbose_name='translation group')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wagtailtranslations.Language', verbose_name='language')),
            ],
            bases=('wagtailcore.page',),
        ),
    ]
