# Generated by Django 4.1.5 on 2024-02-23 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CookieStand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=256)),
                ('cookie_sales', models.IntegerField(default=0)),
                ('avg_cookie_per_hour', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
