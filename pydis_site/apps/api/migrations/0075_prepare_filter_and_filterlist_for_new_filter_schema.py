# Generated by Django 3.0.14 on 2021-12-11 23:14
from django.apps.registry import Apps
from django.db import migrations, models
from django.db.backends.base.schema import BaseDatabaseSchemaEditor


def migrate_filterlist(apps: Apps, schema_editor: BaseDatabaseSchemaEditor) -> None:
    FilterList = apps.get_model("api", "FilterList")
    change_map = {
        "filter_token": "tokens",
        "domain_name": "domains",
        "guild_invite": "invites",
        "file_format": "extensions"
    }
    for filter_list in FilterList.objects.all():
        if change_map.get(filter_list.name):
            filter_list.name = change_map.get(filter_list.name)
            filter_list.save()
    redirects = FilterList(
        name="redirects",
        ping_type=[],
        dm_ping_type=[],
        enabled_channels=[],
        disabled_channels=[],
        disabled_categories=[],
        list_type=0,
        filter_dm=True,
        delete_messages=False,
        bypass_roles=[0],
        enabled=True
    )
    redirects.save()


def unmigrate_filterlist(apps: Apps, schema_editor: BaseDatabaseSchemaEditor) -> None:
    FilterList = apps.get_model("api", "FilterList")
    change_map = {
        "tokens": "filter_token",
        "domains": "domain_name",
        "invites": "guild_invite",
        "formats": "file_format"
    }
    for filter_list in FilterList.objects.all():
        if change_map.get(filter_list.name):
            filter_list.name = change_map.get(filter_list.name)
            filter_list.save()
    FilterList.objects.filter(name="redirects").delete()


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0074_merge_20211017_0822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filter',
            old_name='allowed_categories',
            new_name='disabled_categories',
        ),
        migrations.RenameField(
            model_name='filter',
            old_name='allowed_channels',
            new_name='disabled_channels',
        ),
        migrations.RenameField(
            model_name='filter',
            old_name='disallowed_channels',
            new_name='enabled_channels',
        ),
        migrations.RenameField(
            model_name='filterlist',
            old_name='allowed_categories',
            new_name='disabled_categories',
        ),
        migrations.RenameField(
            model_name='filterlist',
            old_name='allowed_channels',
            new_name='disabled_channels',
        ),
        migrations.RenameField(
            model_name='filterlist',
            old_name='disallowed_channels',
            new_name='enabled_channels',
        ),
        migrations.RemoveField(
            model_name='filterlist',
            name='disallowed_categories',
        ),
        migrations.RemoveField(
            model_name='filter',
            name='disallowed_categories',
        ),
        migrations.RunPython(migrate_filterlist, unmigrate_filterlist)
    ]
