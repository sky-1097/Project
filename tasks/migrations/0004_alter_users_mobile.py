# Generated by Django 5.0.4 on 2024-04-09 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_taskdetail_alter_task_tasktype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
