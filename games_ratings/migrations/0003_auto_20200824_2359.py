# Generated by Django 3.1 on 2020-08-24 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games_ratings', '0002_auto_20200824_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesratings',
            name='game_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='games_ratings.games'),
        ),
    ]
