# Generated by Django 2.0.3 on 2018-03-24 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerLinkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_id', models.SmallIntegerField(unique=True, verbose_name='')),
                ('type_meta', models.CharField(max_length=32, unique=True, verbose_name='')),
                ('type_description', models.CharField(blank=True, max_length=256, null=True, verbose_name='')),
            ],
            options={
                'verbose_name': 'banner跳转类型',
                'verbose_name_plural': 'banner跳转类型',
                'db_table': 'pet_banner_link_type',
            },
        ),
        migrations.CreateModel(
            name='HomeBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('cover', models.CharField(max_length=256, verbose_name='封面')),
                ('link_type', models.SmallIntegerField(verbose_name='跳转类型')),
            ],
            options={
                'verbose_name': '首页banner',
                'verbose_name_plural': '首页banner',
                'db_table': 'pet_home_banner',
            },
        ),
        migrations.CreateModel(
            name='HtmlCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
