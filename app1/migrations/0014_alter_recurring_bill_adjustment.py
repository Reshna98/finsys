# Generated by Django 4.2.2 on 2023-09-26 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_alter_recurring_bill_cgst_alter_recurring_bill_igst_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurring_bill',
            name='adjustment',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
