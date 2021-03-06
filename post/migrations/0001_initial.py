# Generated by Django 3.2.4 on 2021-08-27 10:50

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
                ('name', models.CharField(max_length=120)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to='post.category')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Başlık')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Açıklama')),
                ('post_image', models.ImageField(blank=True, default='default_product.png', null=True, upload_to='', verbose_name='Resim')),
                ('stok', models.IntegerField(default='0', verbose_name='Stok')),
                ('price', models.IntegerField(default='1', verbose_name='Fiyat')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='post.category', verbose_name='Kategori')),
            ],
        ),
    ]
