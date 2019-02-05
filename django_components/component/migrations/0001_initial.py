# Generated by Django 2.1.5 on 2019-02-05 21:22

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=16, unique=True, verbose_name='name')),
                ('view_class', models.CharField(db_index=True, max_length=64, verbose_name='Class-based view')),
                ('path', models.CharField(db_index=True, max_length=64, verbose_name='path')),
                ('kwargs', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='keyword arguments')),
                ('content_type', models.ForeignKey(blank=True, help_text='Blank if type is TemplateView', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='view_set', to='contenttypes.ContentType', verbose_name='content type')),
            ],
            options={
                'verbose_name': 'component',
                'verbose_name_plural': 'components',
            },
        ),
        migrations.AlterIndexTogether(
            name='component',
            index_together={('view_class', 'content_type')},
        ),
    ]