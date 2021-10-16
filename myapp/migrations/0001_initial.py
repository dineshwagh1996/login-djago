# Generated by Django 3.2.7 on 2021-10-16 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='images')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.products')),
            ],
        ),
    ]
