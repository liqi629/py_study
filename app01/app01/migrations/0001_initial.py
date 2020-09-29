# Generated by Django 3.0.8 on 2020-08-19 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('publish', models.CharField(max_length=32)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
