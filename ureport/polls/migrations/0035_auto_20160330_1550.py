# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0034_auto_20160323_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollresult',
            name='org',
            field=models.ForeignKey(related_name='poll_results', to='orgs.Org', db_index=False),
        ),
    ]
