# Generated by Django 4.2.2 on 2023-09-25 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_alter_recurring_bill_adjustment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurring_bill',
            name='cgst',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='recurring_bill',
            name='igst',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='recurring_bill',
            name='sgst',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]