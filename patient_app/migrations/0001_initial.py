# Generated by Django 3.1.1 on 2020-09-10 08:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctor_app', '0002_auto_20200910_0816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookDoctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(blank=True, max_length=100, null=True)),
                ('patient_age', models.IntegerField(default=0)),
                ('patient_gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=100, null=True)),
                ('patient_complaint', models.CharField(blank=True, max_length=200, null=True)),
                ('date_booked', models.DateTimeField(auto_now_add=True)),
                ('appointment_date', models.DateTimeField(auto_now_add=True)),
                ('patient_specialty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctor_app.specialty')),
            ],
        ),
    ]
