# Generated by Django 4.2.7 on 2023-12-06 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapp', '0003_jobposting_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobposting',
            name='employee_id',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
