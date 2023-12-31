# Generated by Django 4.2.7 on 2023-12-12 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0012_remove_paciente_doctor_doctor_paciente_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
    ]
