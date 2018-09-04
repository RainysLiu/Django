# Generated by Django 2.0.6 on 2018-08-09 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('capitcal', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='privence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.country')),
            ],
        ),
    ]
