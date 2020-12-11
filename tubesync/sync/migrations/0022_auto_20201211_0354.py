# Generated by Django 3.1.4 on 2020-12-11 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sync', '0021_auto_20201211_0351'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='downloaded_format',
            field=models.CharField(blank=True, help_text='Audio codec of the downloaded media', max_length=30, null=True, verbose_name='downloaded format'),
        ),
        migrations.AlterField(
            model_name='media',
            name='downloaded_audio_codec',
            field=models.CharField(blank=True, help_text='Audio codec of the downloaded media', max_length=30, null=True, verbose_name='downloaded audio codec'),
        ),
        migrations.AlterField(
            model_name='media',
            name='downloaded_container',
            field=models.CharField(blank=True, help_text='Container format of the downloaded media', max_length=30, null=True, verbose_name='downloaded container format'),
        ),
        migrations.AlterField(
            model_name='media',
            name='downloaded_fps',
            field=models.PositiveSmallIntegerField(blank=True, help_text='FPS of the downloaded media', null=True, verbose_name='downloaded fps'),
        ),
        migrations.AlterField(
            model_name='media',
            name='downloaded_video_codec',
            field=models.CharField(blank=True, help_text='Video codec of the downloaded media', max_length=30, null=True, verbose_name='downloaded video codec'),
        ),
    ]