# Generated by Django 2.2 on 2020-02-29 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=36, unique=True)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('published', models.DateField()),
                ('is_published', models.BooleanField(default=False)),
                ('cover', models.ImageField(upload_to='covers/')),
            ],
        ),
    ]
