# Generated by Django 4.2 on 2025-05-07 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulter', '0002_alter_produit_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='deals',
            field=models.BooleanField(default=False),
        ),
    ]
