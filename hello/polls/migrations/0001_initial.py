# Generated by Django 2.2.5 on 2019-09-17 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(default='image.jpg', upload_to='uploads/')),
                ('price', models.IntegerField(default=None)),
            ],
        ),
    ]