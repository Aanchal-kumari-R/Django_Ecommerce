# Generated by Django 5.0.7 on 2024-11-05 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0008_rename_item_json_order_items_json'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default=' ')),
                ('update_desc', models.CharField(max_length=500)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
