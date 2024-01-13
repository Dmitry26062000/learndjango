# Generated by Django 5.0 on 2024-01-13 15:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Saler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brend_car', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='numOfpower',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='passport',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='yearOfput',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='power',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_price', models.IntegerField(null=True)),
                ('dateOfBuy', models.DateField(auto_now_add=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cars.client')),
                ('num_car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cars.car')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='saler',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cars.saler'),
        ),
    ]
