# Generated by Django 3.2.8 on 2021-10-22 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_alter_userprofile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default='uploads/profile_pictures/default.png', upload_to='uploads/profile_pictures'),
        ),
    ]
