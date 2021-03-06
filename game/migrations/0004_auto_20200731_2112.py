# Generated by Django 3.0.8 on 2020-07-31 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_user_quiz_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='count',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='challenger',
            name='result',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='challenger',
            name='user_obj',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
