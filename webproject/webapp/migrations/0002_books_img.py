# Generated by Django 4.1.7 on 2023-03-08 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='img',
            field=models.ImageField(default=1234, upload_to='pics'),
            preserve_default=False,
        ),
    ]
