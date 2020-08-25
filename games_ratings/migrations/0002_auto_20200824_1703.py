# Generated by Django 3.1 on 2020-08-24 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20200824_1703'),
        ('games_ratings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='rating',
        ),
        migrations.CreateModel(
            name='GamesRatings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games_ratings.games')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.user')),
            ],
        ),
    ]
