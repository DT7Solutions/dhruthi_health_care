# Generated by Django 4.1.3 on 2022-11-21 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeSlider',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Title', models.CharField(default='heading', max_length=25)),
                ('Image', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]
