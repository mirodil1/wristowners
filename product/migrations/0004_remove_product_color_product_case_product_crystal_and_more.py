# Generated by Django 4.0.2 on 2022-06-24 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_image1_product_image2_product_image3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.AddField(
            model_name='product',
            name='case',
            field=models.CharField(blank=True, max_length=155, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='crystal',
            field=models.CharField(blank=True, max_length=155, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, max_length=155, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='strap',
            field=models.CharField(blank=True, max_length=155, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='bazel',
            field=models.CharField(blank=True, max_length=155, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='clasp',
            field=models.CharField(blank=True, max_length=155, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='movement',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='series',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]
