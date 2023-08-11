# Generated by Django 4.2.4 on 2023-08-11 20:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_recipe_instructions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(choices=[('Wi', 'White'), ('LP', 'Light Purple'), ('LB', 'Light Blue'), ('Rd', 'Red'), ('Yw', 'Yellow'), ('Gn', 'Green'), ('Or', 'Orange'), ('Pk', 'Pink'), ('Ba', 'Black'), ('Tl', 'Teal'), ('LG', 'Light Grey'), ('DG', 'Dark Grey'), ('DB', 'Dark Blue'), ('Mr', 'Maroon'), ('Gl', 'Gold'), ('DP', 'Dark Purple')], default='Wi', max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default='New Ingredient', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(related_name='recipes', to='main_app.tag'),
        ),
    ]
