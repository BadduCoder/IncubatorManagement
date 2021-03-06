# Generated by Django 2.1.7 on 2019-02-14 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0002_startuplog'),
        ('rooms', '0002_auto_20190214_0920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_issued', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='room',
            name='number',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AddField(
            model_name='seat',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.Room'),
        ),
        migrations.AddField(
            model_name='seat',
            name='startup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='startups.Startup'),
        ),
    ]
