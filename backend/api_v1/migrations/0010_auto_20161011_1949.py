# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 19:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0009_experiment_is_valid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polarization', models.CharField(choices=[('horizontal', 'Horizontal'), ('vertical', 'Vertical'), ('cross', 'Cross'), ('mixed', 'Mixed')], max_length=15)),
                ('device', models.CharField(choices=[('computer-1', 'Computer 1'), ('computer-2', 'Computer 2')], max_length=50)),
                ('order', models.CharField(max_length=70, null=True)),
                ('start', models.DateTimeField(null=True)),
                ('end', models.DateTimeField(null=True)),
                ('white_start', models.DateTimeField(null=True)),
                ('white_end', models.DateTimeField(null=True)),
                ('blue_start', models.DateTimeField(null=True)),
                ('blue_end', models.DateTimeField(null=True)),
                ('red_start', models.DateTimeField(null=True)),
                ('red_end', models.DateTimeField(null=True)),
                ('is_valid', models.NullBooleanField()),
            ],
            options={
                'verbose_name': 'Trial',
                'verbose_name_plural': 'Trials',
                'ordering': ['-start'],
            },
        ),
        migrations.AlterModelOptions(
            name='experiment',
            options={'ordering': ['last_name', 'first_name', 'age', '-experiment_start'], 'verbose_name': 'Experiment', 'verbose_name_plural': 'Experiments'},
        ),
        migrations.AlterField(
            model_name='experiment',
            name='device',
            field=models.CharField(choices=[('computer-1', 'Computer 1'), ('computer-2', 'Computer 2')], max_length=50),
        ),
        migrations.AddField(
            model_name='trial',
            name='experiment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiment.Experiment'),
        ),
    ]
