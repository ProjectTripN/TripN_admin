# Generated by Django 3.2.5 on 2021-12-28 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateField()),
                ('people', models.IntegerField()),
                ('day', models.IntegerField()),
                ('plane_unit', models.IntegerField()),
                ('plane_price', models.IntegerField()),
                ('acc_unit', models.IntegerField()),
                ('acc_price', models.IntegerField()),
                ('act_unit', models.IntegerField()),
                ('price', models.IntegerField()),
                ('tax', models.IntegerField()),
                ('subtotal', models.IntegerField()),
                ('fees', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('jeju_schedule', models.IntegerField()),
                ('user', models.IntegerField()),
            ],
            options={
                'db_table': 'reservation',
            },
        ),
    ]