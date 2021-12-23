# Generated by Django 3.1 on 2021-03-04 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0023_auto_20210304_1303'),
        ('comments', '0014_auto_20210304_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='person',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='talent.person'),
        ),
    ]