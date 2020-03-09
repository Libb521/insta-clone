# Generated by Django 3.0.4 on 2020-03-08 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gram', '0006_auto_20200308_1559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='commenter',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='comment_post',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='image',
            new_name='commented_image',
        ),
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.PositiveIntegerField(default=0, verbose_name='Likes'),
        ),
        migrations.AddField(
            model_name='image',
            name='tag_someone',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='User',
            field=models.OneToOneField(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_avatar',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='Apic/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
    ]