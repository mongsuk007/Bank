# Generated by Django 3.0.6 on 2020-07-14 02:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('validators', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ValidatorConfirmationService',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('end', models.DateTimeField()),
                ('start', models.DateTimeField()),
                ('validator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='validator_confirmation_services', to='validators.Validator')),
            ],
            options={
                'default_related_name': 'validator_confirmation_services',
            },
        ),
    ]
