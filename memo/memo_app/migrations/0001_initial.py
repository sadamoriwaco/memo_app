# Generated by Django 3.2.9 on 2022-11-10 08:01

from django.db import migrations, models
import django.db.models.deletion
import memo_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Custmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100, validators=[memo_app.models.number_only])),
                ('name', models.CharField(max_length=100, validators=[memo_app.models.number_only])),
                ('mail', models.EmailField(max_length=200)),
                ('gender', models.BooleanField()),
                ('visitday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=300)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('custmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memo_app.custmer')),
            ],
            options={
                'ordering': ('pub_date',),
            },
        ),
    ]
