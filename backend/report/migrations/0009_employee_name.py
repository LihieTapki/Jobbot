# Generated by Django 4.2.3 on 2023-08-31 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0008_rename_report_workreport_alter_workreport_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='name',
            field=models.CharField(default='nick', help_text='укажите имя cотрудника латиницей', max_length=150, verbose_name='Имя сотрудника'),
        ),
    ]
