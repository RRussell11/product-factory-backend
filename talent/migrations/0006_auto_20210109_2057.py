# Generated by Django 3.1 on 2021-01-09 20:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0005_person_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='productperson',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='personprofile',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='review',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]