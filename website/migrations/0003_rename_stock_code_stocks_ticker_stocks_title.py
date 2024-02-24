# Generated by Django 5.0.2 on 2024-02-24 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_tickercode_remove_stocks_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stocks',
            old_name='stock_code',
            new_name='ticker',
        ),
        migrations.AddField(
            model_name='stocks',
            name='title',
            field=models.CharField(default='test', max_length=40),
            preserve_default=False,
        ),
    ]