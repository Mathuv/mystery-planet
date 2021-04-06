# Generated by Django 3.1.7 on 2021-04-06 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0006_auto_20210406_0746'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='friends',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='friends',
            name='friend',
        ),
        migrations.RemoveField(
            model_name='friends',
            name='person',
        ),
        migrations.AddField(
            model_name='person',
            name='favourite_foods',
            field=models.ManyToManyField(blank=True, null=True, to='persons.Food'),
        ),
        migrations.AddField(
            model_name='person',
            name='friends',
            field=models.ManyToManyField(blank=True, null=True, related_name='_person_friends_+', to='persons.Person'),
        ),
        migrations.DeleteModel(
            name='FavouriteFoods',
        ),
        migrations.DeleteModel(
            name='Friends',
        ),
    ]