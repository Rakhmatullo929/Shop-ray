# Generated by Django 4.1.7 on 2023-08-27 13:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("store", "0003_slide"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Cart",
            new_name="CartProduct",
        ),
    ]
