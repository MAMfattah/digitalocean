# Generated by Django 3.0.14 on 2021-08-30 21:09

from django.db import migrations, models
import pydis_site.apps.api.models.bot.documentation_link


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0071_increase_message_content_4000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentationlink',
            name='base_url',
            field=models.URLField(blank=True, help_text='The base URL from which documentation will be available for this project. Used to generate links to various symbols within this package.', validators=[pydis_site.apps.api.models.bot.documentation_link.ends_with_slash_validator]),
        ),
    ]
