# Generated by Django 4.2.1 on 2023-05-11 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_mainphoto_post_imgfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_pic', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='imgfile',
        ),
    ]
