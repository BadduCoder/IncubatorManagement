# Generated by Django 2.1.7 on 2019-02-15 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20190214_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='startup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='startups.Startup'),
        ),
    ]