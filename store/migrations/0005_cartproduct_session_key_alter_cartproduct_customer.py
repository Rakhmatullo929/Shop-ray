# Generated by Django 4.1.7 on 2023-08-27 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("store", "0004_rename_cart_cartproduct"),
    ]

    operations = [
        migrations.AddField(
            model_name="cartproduct",
            name="session_key",
            field=models.CharField(
                blank=True, max_length=1024, null=True, verbose_name="Ключ сессии"
            ),
        ),
        migrations.AlterField(
            model_name="cartproduct",
            name="customer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
