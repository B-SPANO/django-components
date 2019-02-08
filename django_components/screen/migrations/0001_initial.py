# Generated by Django 2.1.5 on 2019-02-08 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('component', '0001_initial'),
        ('template', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Layout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block', models.CharField(db_index=True, help_text='Name of the spot the component should be inserted into.', max_length=127, verbose_name='block name')),
                ('order', models.IntegerField(db_index=True, help_text='If many components are set to get into the same spot, the first one to get there is the lower.', verbose_name='block order')),
                ('component', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='layout_set', to='component.Component', verbose_name='component')),
            ],
            options={
                'verbose_name': 'layout',
                'verbose_name_plural': 'layouts',
            },
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(db_index=True, help_text='used in html head and H1 (you can use templating language)', max_length=127, verbose_name='screen label')),
                ('icon', models.CharField(help_text='icon name, according to your CSS framework - used as visual identification everywhere it should', max_length=16, verbose_name='CSS icon name')),
                ('hide_in_sitemap', models.BooleanField(default=False, verbose_name='Should this screen be hidden in sitemap ?')),
                ('component_set', models.ManyToManyField(through='screen.Layout', to='component.Component')),
                ('comprehensive', models.ForeignKey(blank=True, help_text='set the comprehensive screen of which this current screen is a specific version of', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='specific_set', to='screen.Screen', verbose_name='overloaded screen')),
                ('parent', models.ForeignKey(blank=True, help_text='parent menu item', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_set', to='screen.Screen', verbose_name='parent')),
                ('template', models.ForeignKey(help_text='set the comprehensive screen of which this current screen is a specific version of', on_delete=django.db.models.deletion.CASCADE, related_name='screen_set', to='template.Template', verbose_name='template')),
            ],
            options={
                'verbose_name': 'screen',
                'verbose_name_plural': 'screens',
            },
        ),
        migrations.AddField(
            model_name='layout',
            name='screen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='layout_set', to='screen.Screen', verbose_name='screen'),
        ),
        migrations.AlterUniqueTogether(
            name='screen',
            unique_together={('parent', 'label')},
        ),
        migrations.AlterIndexTogether(
            name='screen',
            index_together={('comprehensive', 'label'), ('parent', 'comprehensive', 'label'), ('parent', 'label')},
        ),
        migrations.AlterUniqueTogether(
            name='layout',
            unique_together={('screen', 'component', 'block')},
        ),
        migrations.AlterIndexTogether(
            name='layout',
            index_together={('screen', 'component'), ('screen', 'component', 'block'), ('screen', 'component', 'block', 'order')},
        ),
    ]
