# Generated by Django 2.0.5 on 2018-06-14 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicsite', '0004_facebook_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facebook',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]