# Generated by Django 3.1.3 on 2021-01-25 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('name', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('name_fr', models.CharField(max_length=250)),
                ('url', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ProdCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ProdStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('code', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('url', models.TextField(null=True)),
                ('quantity', models.CharField(max_length=250, null=True)),
                ('brand', models.CharField(max_length=250, null=True)),
                ('country', models.CharField(max_length=250)),
                ('ingredients', models.TextField(null=True)),
                ('energy', models.IntegerField(null=True)),
                ('fat', models.IntegerField(null=True)),
                ('satured_fat', models.IntegerField(null=True)),
                ('carbohydrates', models.IntegerField(null=True)),
                ('sugar', models.IntegerField(null=True)),
                ('fibers', models.IntegerField(null=True)),
                ('proteins', models.IntegerField(null=True)),
                ('salt', models.IntegerField(null=True)),
                ('sodium', models.IntegerField(null=True)),
                ('nutriscore', models.CharField(max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RelatedCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Stores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('brand', models.CharField(max_length=250, null=True)),
                ('city', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserSave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('compared_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='compared_product', to='products.products')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_saved', to='products.products')),
            ],
        ),
    ]
