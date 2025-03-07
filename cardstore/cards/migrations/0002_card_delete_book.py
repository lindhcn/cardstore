# Generated by Django 5.1.4 on 2025-02-02 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('isbn', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
