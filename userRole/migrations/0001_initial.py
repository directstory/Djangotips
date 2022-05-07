# Generated by Django 4.0.4 on 2022-05-07 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RolesFearutes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read', models.BooleanField(default=False)),
                ('write', models.BooleanField(default=False)),
                ('delete', models.BooleanField(default=False)),
                ('feature_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userRole.features')),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userRole.roles')),
            ],
        ),
        migrations.AddField(
            model_name='roles',
            name='features',
            field=models.ManyToManyField(through='userRole.RolesFearutes', to='userRole.features'),
        ),
    ]
