# Generated by Django 2.0.7 on 2019-08-20 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HitsDatePoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(auto_now=True, db_index=True)),
                ('hits', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('short_link', models.URLField(default='')),
                ('hits', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='hitsdatepoint',
            name='link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiny_link.Link'),
        ),
        migrations.AlterUniqueTogether(
            name='hitsdatepoint',
            unique_together={('day', 'link')},
        ),
    ]
