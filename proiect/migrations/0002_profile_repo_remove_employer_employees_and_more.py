# Generated by Django 4.0.4 on 2022-05-14 21:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('proiect', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.CharField(max_length=60)),
                ('fullname', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('bio', models.CharField(max_length=200)),
                ('followers', models.IntegerField()),
                ('following', models.IntegerField()),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'profiles',
            },
        ),
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=60, unique=True)),
                ('language', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proiect.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'repos',
            },
        ),
        migrations.RemoveField(
            model_name='employer',
            name='employees',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Employer',
        ),
        migrations.AddField(
            model_name='profile',
            name='repos',
            field=models.ManyToManyField(related_name='repos', through='proiect.Repo', to=settings.AUTH_USER_MODEL),
        ),
    ]