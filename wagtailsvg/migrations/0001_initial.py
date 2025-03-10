# Generated by Django 3.1.4 on 2020-12-05 09:36

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import wagtail.core.models
import wagtail.search.index


class Migration(migrations.Migration):

    initial = True

    dependencies = [
       # ('wagtailcore', '0059_apply_collection_ordering'),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Svg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('file', models.FileField(upload_to='media', verbose_name='file')),
                ('collection', models.ForeignKey(default=wagtail.core.models.get_root_collection_id, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.collection', verbose_name='collection')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text=None, through='taggit.TaggedItem', to='taggit.Tag', verbose_name='tags')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
    ]
