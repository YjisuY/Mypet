# Generated by Django 4.2.1 on 2023-05-13 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_delete_examplemodel_post_imgfile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='imgfile',
            new_name='images',
        ),
    ]
