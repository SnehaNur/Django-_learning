# Generated by Django 5.2 on 2025-04-10 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_address_zip'),
    ]

    operations = [
        migrations.RunSQL("""
            INSERT INTO store_collection (title)
            VALUES ('collection1')             
        ""","""
            DELETE FROM store_collection
            WHERE title='collection1'
        """)
    ]
