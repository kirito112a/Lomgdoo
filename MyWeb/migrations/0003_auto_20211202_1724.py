# Generated by Django 3.2.8 on 2021-12-02 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyWeb', '0002_alter_answer_answer_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_and_service',
            name='product_option_gender',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product_and_service',
            name='product_option_province',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
