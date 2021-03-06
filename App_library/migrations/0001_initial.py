# Generated by Django 3.2 on 2021-04-07 16:50

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('cover', models.ImageField(upload_to='book_cover')),
                ('author', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, max_length=25000, null=True)),
                ('available', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='BookLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('self_no', models.CharField(max_length=255)),
                ('row_no', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NID', models.CharField(max_length=255, unique=True)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=17, null=True, validators=[django.core.validators.RegexValidator(message='Enter a valid Bangladesh mobile phone number starting with +(country code)', regex='^\\+?(88)01[3-9][0-9]{8}$')], verbose_name='Mobile phone')),
                ('year', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.date.today)),
                ('status', models.CharField(max_length=25)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_library.book')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_library.customer')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_library.category'),
        ),
        migrations.AddField(
            model_name='book',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_location', to='App_library.booklocation'),
        ),
    ]
