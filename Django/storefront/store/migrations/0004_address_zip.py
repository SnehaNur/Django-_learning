# Generated by Django 5.2 on 2025-04-09 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_add_slug_to_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.CharField(default='null', max_length=255),
            preserve_default=False,
        ),
    ]
