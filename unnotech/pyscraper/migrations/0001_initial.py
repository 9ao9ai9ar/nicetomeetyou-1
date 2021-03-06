# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-12 17:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_text', models.CharField(max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='Headline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='headline',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pyscraper.Headline'),
        ),
    ]
