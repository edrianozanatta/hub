# Generated by Django 2.1.3 on 2019-01-06 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0003_auto_20190106_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
