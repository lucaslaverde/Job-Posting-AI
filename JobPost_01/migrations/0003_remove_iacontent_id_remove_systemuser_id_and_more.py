# Generated by Django 5.0.7 on 2024-10-23 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobPost_01', '0002_systemuser_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iacontent',
            name='id',
        ),
        migrations.RemoveField(
            model_name='systemuser',
            name='id',
        ),
        migrations.AlterField(
            model_name='iacontent',
            name='Empresa',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='systemuser',
            name='Usuario',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]
