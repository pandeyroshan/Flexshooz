# Generated by Django 2.0 on 2020-03-21 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('management', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='CheckOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=300)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Checkout',
                'verbose_name_plural': 'Checkout',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('tagline', models.CharField(max_length=300, verbose_name='Tagline')),
                ('description', models.TextField()),
                ('product_code', models.CharField(max_length=15)),
                ('price', models.IntegerField(default=1200, verbose_name='Price')),
                ('img1', models.ImageField(upload_to='Product Images', verbose_name='Image 1')),
                ('img2', models.ImageField(upload_to='Product Images', verbose_name='Image 2')),
                ('img3', models.ImageField(upload_to='Product Images', verbose_name='Image 3')),
                ('img4', models.ImageField(upload_to='Product Images', verbose_name='Image 4')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
            options={
                'verbose_name': 'Products',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='shoe_color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=20, verbose_name='Colors')),
            ],
            options={
                'verbose_name': 'Colors',
                'verbose_name_plural': 'Colors',
            },
        ),
        migrations.CreateModel(
            name='shoe_size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=8, verbose_name='Shoe Number')),
            ],
            options={
                'verbose_name': 'Shoe Numbers',
                'verbose_name_plural': 'Shoe Numbers',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='shoe_color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.shoe_color'),
        ),
        migrations.AddField(
            model_name='product',
            name='shoe_size',
            field=models.ManyToManyField(related_name='sizeofshoe', to='store.shoe_size'),
        ),
        migrations.AddField(
            model_name='checkout',
            name='Product',
            field=models.ManyToManyField(related_name='shoes', to='store.Product'),
        ),
        migrations.AddField(
            model_name='checkout',
            name='University',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.University'),
        ),
        migrations.AddField(
            model_name='checkout',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
