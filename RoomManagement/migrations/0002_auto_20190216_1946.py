# Generated by Django 2.1.7 on 2019-02-16 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RoomManagement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='seats',
        ),
        migrations.AddField(
            model_name='seat',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='RoomManagement.Room'),
        ),
    ]
