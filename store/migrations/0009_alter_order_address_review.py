# Generated by Django 4.2.1 on 2023-09-15 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0008_order_orderproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(choices=[('Город Бухара', 'Город Бухара'), ('Ромитанский район', 'Ромитанский район'), ('Гиждуванский район', 'Гиждуванский район'), ('Жондорский район', 'Жондорский район'), ('Каганский район', 'Каганский район'), ('Шафирканский район', 'Шафирканский район'), ('Вабкентский район', 'Вабкентский район'), ('Алатский район', 'Алатский район')], max_length=255),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, '⭐️'), (2, '⭐️ ⭐️'), (3, '⭐️ ⭐️ ⭐️'), (4, '⭐️ ⭐️ ⭐️ ⭐️'), (5, '⭐️ ⭐️ ⭐️ ⭐️ ⭐️')], null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
