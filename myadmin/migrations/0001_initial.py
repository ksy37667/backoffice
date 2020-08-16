# Generated by Django 3.1 on 2020-08-16 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('dept_no', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'db_table': 'departments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('emp_no', models.IntegerField(primary_key=True, serialize=False)),
                ('birth_date', models.DateField()),
                ('first_name', models.CharField(max_length=14)),
                ('last_name', models.CharField(max_length=16)),
                ('gender', models.CharField(max_length=1)),
                ('hire_date', models.DateField()),
            ],
            options={
                'db_table': 'employees',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DeptEmp',
            fields=[
                ('emp_no', models.OneToOneField(db_column='emp_no', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='myadmin.employees')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
            ],
            options={
                'db_table': 'dept_emp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DeptManager',
            fields=[
                ('emp_no', models.OneToOneField(db_column='emp_no', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='myadmin.employees')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
            ],
            options={
                'db_table': 'dept_manager',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Salaries',
            fields=[
                ('emp_no', models.OneToOneField(db_column='emp_no', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='myadmin.employees')),
                ('salary', models.IntegerField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
            ],
            options={
                'db_table': 'salaries',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('emp_no', models.OneToOneField(db_column='emp_no', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='myadmin.employees')),
                ('title', models.CharField(max_length=50)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'titles',
                'managed': False,
            },
        ),
    ]