# Generated by Django 3.2.8 on 2021-10-18 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_profile_use_choice_con'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country_Master',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='degree_Master',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='faculty_Master',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='gpa_Master',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='graduate_Master',
            field=models.DateField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='profile',
            name='honors_Master',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='province_Master',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='study_date_Master',
            field=models.DateField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='profile',
            name='university_Master',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='use_choice_con_Master',
            field=models.CharField(blank=True, choices=[('?????????', '?????????'), ('??????????????????', '??????????????????')], max_length=9, null=True),
        ),
    ]
