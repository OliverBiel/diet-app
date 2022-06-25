# Generated by Django 4.0.5 on 2022-06-25 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meals', '0002_alter_meal_foods'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('meals', models.ManyToManyField(to='meals.meal')),
            ],
        ),
    ]
