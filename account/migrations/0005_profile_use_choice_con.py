# Generated by Django 3.2.8 on 2021-10-18 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_profile_degree'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='use_choice_con',
            field=models.CharField(blank=True, choices=[('ใช้', 'ใช้'), ('ไม่ใช้', 'ไม่ใช้')], max_length=9, null=True),
        ),
    ]