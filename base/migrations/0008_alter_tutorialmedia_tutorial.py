# Generated by Django 3.2.9 on 2022-06-14 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_tutorialmedia_tutorial_videos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorialmedia',
            name='tutorial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutorial_id', to='base.tutorial'),
        ),
    ]