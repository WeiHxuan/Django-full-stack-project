# Generated by Django 4.0.5 on 2022-06-30 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('mid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('click', models.IntegerField()),
                ('id', models.TextField()),
                ('phone_img', models.TextField()),
                ('market_price', models.TextField()),
                ('sell_price', models.TextField()),
                ('stock_quantity', models.IntegerField()),
                ('disposition', models.TextField()),
                ('release_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
