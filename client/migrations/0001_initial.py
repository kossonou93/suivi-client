# Generated by Django 4.2.4 on 2023-09-02 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]