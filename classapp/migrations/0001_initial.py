# Generated by Django 4.1.2 on 2022-10-13 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('img', models.ImageField(default='category/pic.jpg', upload_to='category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=50)),
                ('p_model', models.CharField(max_length=50)),
                ('p_price', models.IntegerField()),
                ('p_img', models.ImageField(default='product/pix.jpg', upload_to='product')),
                ('des', models.TextField()),
                ('trending', models.BooleanField()),
                ('latest', models.BooleanField()),
                ('p_min', models.IntegerField()),
                ('p_max', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.category')),
            ],
        ),
    ]
