# Generated by Django 2.1.7 on 2019-04-05 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20190404_0847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(choices=[('EVENT1 TECHNICAL', 'EVENT1 TECHNICAL'), ('EVENT2 TECHNICAL', 'EVENT2 TECHNICAL'), ('EVENT3 TECHNICAL', 'EVENT3 TECHNICAL'), ('EVENT4 TECHNICAL', 'EVENT4 TECHNICAL'), ('EVENT5 TECHNICAL', 'EVENT5 TECHNICAL'), ('EVENT6 NON-TECHNICAL', 'EVENT6 NON-TECHNICAL'), ('EVENT7 NON-TECHNICAL', 'EVENT7 NON-TECHNICAL'), ('EVENT8 NON-TECHNICAL', 'EVENT8 NON-TECHNICAL'), ('EVENT9 NON-TECHNICAL', 'EVENT9 NON-TECHNICAL'), ('EVENT10 NON-TECHNICAL', 'EVENT10 NON-TECHNICAL')], help_text='Enter Event Name (e.g. CodeGolf Teechnical)', max_length=200)),
            ],
        ),
    ]
