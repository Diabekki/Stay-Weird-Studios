# Generated by Django 3.2 on 2022-01-12 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='original_cart',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='purchase',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]
