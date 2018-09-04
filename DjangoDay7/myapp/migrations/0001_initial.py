# Generated by Django 2.0.6 on 2018-08-14 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('author', models.CharField(max_length=10)),
                ('price', models.FloatField()),
            ],
        ),
    ]