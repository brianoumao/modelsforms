# Generated by Django 5.0.2 on 2024-02-28 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('date_of_birth', models.DateField()),
            ],
            options={
                'db_table': 'Students',
            },
        ),
    ]