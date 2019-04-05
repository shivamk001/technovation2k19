# Generated by Django 2.1.7 on 2019-04-04 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Event')),
            ],
        ),
        migrations.RemoveField(
            model_name='prticipation',
            name='event',
        ),
        migrations.RemoveField(
            model_name='prticipation',
            name='participant',
        ),
        migrations.AddField(
            model_name='profile',
            name='college',
            field=models.CharField(default='IERT', max_length=100),
        ),
        migrations.DeleteModel(
            name='Prticipation',
        ),
        migrations.AddField(
            model_name='participation',
            name='participant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Profile'),
        ),
    ]
