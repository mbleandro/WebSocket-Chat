# Generated by Django 2.2 on 2021-07-29 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210720_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='avatar',
            field=models.URLField(default='https://filestore.community.support.microsoft.com/api/images/6061bd47-2818-4f2b-b04a-5a9ddb6f6467?upload=true'),
        ),
    ]