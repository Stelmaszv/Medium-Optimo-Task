# Generated by Django 3.1.3 on 2022-06-18 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20220618_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='Author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.author'),
        ),
    ]
