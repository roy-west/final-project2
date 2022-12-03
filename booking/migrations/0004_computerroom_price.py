# Generated by Django 4.1.3 on 2022-12-03 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_rename_computer_order_computers'),
    ]

    operations = [
        migrations.AddField(
            model_name='computerroom',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=10),
            preserve_default=False,
        ),
    ]
