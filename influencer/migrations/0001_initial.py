# Generated by Django 2.0.3 on 2018-06-11 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvTrx',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('insert_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='InfluencerSummary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('insert_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('trx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='influencer.AdvTrx')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]