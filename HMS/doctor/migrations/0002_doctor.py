# Generated by Django 3.0.5 on 2020-05-25 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=13, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=128, null=True)),
                ('age', models.CharField(max_length=3, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('department', models.CharField(choices=[('Oncology', 'Oncology'), ('Neurology', 'Neurology'), ('OPD', 'OPD')], max_length=128, null=True)),
                ('attendence', models.CharField(max_length=100, null=True)),
                ('salary', models.CharField(max_length=128, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=128, null=True)),
                ('user', models.OneToOneField(blank=True, limit_choices_to={'groups__name': 'Patients'}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
