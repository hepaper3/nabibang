# Generated by Django 2.2.4 on 2019-08-04 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190804_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
