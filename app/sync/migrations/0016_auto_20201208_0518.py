# Generated by Django 3.1.4 on 2020-12-08 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sync', '0015_auto_20201207_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='fallback',
            field=models.CharField(choices=[('f', 'Fail, do not download any media'), ('n', 'Get next best resolution or codec instead'), ('h', 'Get next best resolution but at least HD')], db_index=True, default='h', help_text='What do do when media in your source resolution and codecs is not available', max_length=1, verbose_name='fallback'),
        ),
    ]
