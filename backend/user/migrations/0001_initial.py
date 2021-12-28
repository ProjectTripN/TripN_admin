# Generated by Django 3.2.5 on 2021-12-27 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('birth', models.DateField()),
                ('card_company', models.TextField()),
                ('card_number', models.IntegerField()),
                ('email', models.TextField()),
                ('first_name', models.TextField()),
                ('gender', models.TextField()),
                ('last_name', models.TextField()),
                ('mbti', models.TextField()),
                ('mbti_list', models.TextField()),
                ('name', models.TextField()),
                ('passport', models.TextField()),
                ('password', models.TextField()),
                ('phone_number', models.TextField()),
                ('reg_date', models.DateField()),
                ('username', models.TextField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]