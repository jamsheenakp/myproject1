# Generated by Django 3.1.7 on 2021-04-05 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=50)),
                ('branch_place', models.CharField(max_length=50)),
                ('branch_city', models.CharField(max_length=50)),
                ('branch_phone', models.CharField(max_length=50)),
                ('branch_image', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_price', models.CharField(max_length=50)),
                ('item_quantity', models.CharField(max_length=50)),
                ('item_image', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('usertype', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='order_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('total_amount', models.CharField(max_length=50)),
                ('return_date', models.DateField(max_length=50)),
                ('no_of_days', models.CharField(max_length=50)),
                ('CUSTOMER_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding_rental.customer')),
            ],
        ),
        migrations.CreateModel(
            name='subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_name', models.CharField(max_length=50)),
                ('CATEGORY_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding_rental.category')),
            ],
        ),
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=50)),
                ('BRANCH_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding_rental.branch')),
                ('ITEM_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding_rental.item')),
            ],
        ),
        migrations.CreateModel(
            name='rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=50)),
                ('review', models.CharField(max_length=100)),
                ('CUSTOMER_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding_rental.customer')),
                ('ITEM_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding_rental.item')),
            ],
        ),
        migrations.CreateModel(
            name='order_sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=50)),
                ('ITEM_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding_rental.item')),
                ('ORDER_MASTER_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding_rental.order_master')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='SUBCATEGORY_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding_rental.subcategory'),
        ),
        migrations.CreateModel(
            name='damage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('damage', models.CharField(max_length=50)),
                ('ITEM_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding_rental.item')),
                ('order_sub_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding_rental.order_sub')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='LOGIN_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding_rental.login'),
        ),
        migrations.CreateModel(
            name='complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=100)),
                ('replay', models.CharField(max_length=100)),
                ('date', models.DateField(max_length=50)),
                ('CUSTOMER_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding_rental.customer')),
            ],
        ),
        migrations.CreateModel(
            name='cash_entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('date', models.DateField(max_length=50)),
                ('DAMAGE_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding_rental.damage')),
                ('ORDER_MASTER_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding_rental.order_master')),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=50)),
                ('CUSTOMER_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding_rental.customer')),
                ('ITEM_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding_rental.item')),
            ],
        ),
        migrations.CreateModel(
            name='branch_manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('house_name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=200)),
                ('BRANCH_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding_rental.branch')),
                ('LOGIN_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding_rental.login')),
            ],
        ),
    ]
