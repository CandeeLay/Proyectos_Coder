# Generated by Django 4.2.2 on 2023-06-30 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_user_empresa_edad_user_empresa_contacto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='crear_empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('experiencia', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='user_empresa',
            new_name='crear_empresa',
        ),
        migrations.DeleteModel(
            name='user_empleado',
        ),
    ]