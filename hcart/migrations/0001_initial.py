# Generated by Django 4.1.1 on 2023-03-10 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=20)),
                ('customer_email', models.CharField(max_length=30)),
                ('address', models.CharField(default='', max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('cust_phone', models.BigIntegerField()),
                ('cust_pass', models.CharField(max_length=8)),
                ('cust_pic', models.ImageField(default='customer/profil.webp', upload_to='customer/')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_name', models.CharField(max_length=20)),
                ('seller_add', models.CharField(max_length=50)),
                ('seller_gen', models.CharField(max_length=20)),
                ('seller_pho', models.BigIntegerField()),
                ('comp_name', models.CharField(max_length=50)),
                ('acc_hold', models.CharField(max_length=20)),
                ('ifsc', models.CharField(max_length=20)),
                ('branch', models.CharField(max_length=20)),
                ('acc_num', models.BigIntegerField()),
                ('email', models.CharField(max_length=50)),
                ('seller_usr', models.CharField(max_length=30)),
                ('seller_pass', models.CharField(max_length=20)),
                ('seller_pic', models.ImageField(upload_to='seller/')),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
    ]