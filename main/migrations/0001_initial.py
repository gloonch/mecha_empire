# Generated by Django 2.2 on 2020-04-04 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bullet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('sniper', models.IntegerField(default=0)),
                ('assualt', models.IntegerField(default=0)),
                ('engineer', models.IntegerField(default=0)),
                ('support', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'bullet',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('total_kill', models.IntegerField(default=0)),
                ('total_death', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('rank', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('coin', models.IntegerField(default=0)),
                ('extra_health', models.IntegerField(default=0)),
                ('special_attacks', models.IntegerField(default=0)),
                ('bullet', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.Bullet')),
            ],
            options={
                'db_table': 'wallet',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('created_at', models.DateField(auto_created=True, auto_now=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nickname', models.TextField(default='guest')),
                ('phone_number', models.TextField(default='000000000', max_length=10, unique=True)),
                ('token', models.TextField(default='', null=True, unique=True)),
                ('last_code_send', models.IntegerField(blank=True, default=0, null=True)),
                ('avatar_url', models.TextField(blank=True, null=True)),
                ('profile', models.ForeignKey(db_column='profile', on_delete=django.db.models.deletion.DO_NOTHING, to='main.Profile')),
                ('wallet', models.ForeignKey(db_column='wallet', on_delete=django.db.models.deletion.DO_NOTHING, to='main.Wallet')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
