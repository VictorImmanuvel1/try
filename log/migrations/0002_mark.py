# Generated by Django 2.1.7 on 2021-03-23 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m1', models.FloatField(null=True)),
                ('m2', models.FloatField(null=True)),
                ('m3', models.FloatField(null=True)),
                ('mid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='log.User')),
            ],
        ),
    ]
