# Generated by Django 4.2 on 2023-09-29 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('price', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('instock', models.CharField(max_length=50)),
            ],
        ),
    ]
