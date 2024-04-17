# Generated by Django 3.2.25 on 2024-04-13 06:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import envoy_translator.listeners.models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listener',
            fields=[
                ('uuid', models.CharField(default=envoy_translator.listeners.models.hex_uuid, max_length=32, primary_key=True, serialize=False)),
                ('listener_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=512)),
                ('ip', models.CharField(max_length=40)),
                ('external_ip', models.CharField(max_length=40)),
                ('port', models.IntegerField(default=0)),
                ('type', models.CharField(default=0, max_length=20)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'unique_together': {('ip', 'port')},
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('uuid', models.CharField(default=envoy_translator.listeners.models.hex_uuid, max_length=32, primary_key=True, serialize=False)),
                ('domain_names', models.TextField()),
                ('keystone_user', jsonfield.fields.JSONField(default={})),
                ('project_id', models.CharField(max_length=64, null=True)),
                ('target_servers', jsonfield.fields.JSONField(default=[])),
                ('listener', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listeners.listener')),
            ],
        ),
    ]
