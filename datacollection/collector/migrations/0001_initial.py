# Generated by Django 2.2 on 2019-04-10 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder_number', models.CharField(max_length=255)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('education', models.CharField(max_length=255)),
                ('occupation', models.CharField(max_length=255)),
                ('income', models.IntegerField()),
                ('marital_status', models.CharField(max_length=255)),
                ('immunization', models.TextField(max_length=255)),
                ('remarks', models.TextField()),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collector.Family')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinical_details', models.TextField()),
                ('diagnosis', models.TextField()),
                ('date', models.DateField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collector.Member')),
            ],
        ),
    ]
