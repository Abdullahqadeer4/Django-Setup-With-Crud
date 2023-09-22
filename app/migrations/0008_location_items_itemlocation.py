# Generated by Django 4.2.5 on 2023-09-22 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locationname', models.CharField(max_length=30, unique=True)),
                ('ltype', models.CharField(max_length=50)),
                ('lserial', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='items',
            name='itemlocation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.location'),
            preserve_default=False,
        ),
    ]
