# Generated by Django 3.1.1 on 2020-11-14 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porta_z', '0007_auto_20201114_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='color_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_col', models.PositiveIntegerField()),
                ('position', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=255, verbose_name='Имя категории')),
            ],
        ),
    ]