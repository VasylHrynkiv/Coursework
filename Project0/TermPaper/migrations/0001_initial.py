from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_name', models.CharField(max_length=20, verbose_name='Developer')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pack_name', models.CharField(max_length=20, verbose_name='Package')),
            ],
        ),
        migrations.CreateModel(
            name='Gen_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('launched', models.IntegerField(max_length=20, verbose_name='Launched(year)')),
                ('clock_rate', models.CharField(max_length=20, verbose_name='Clock_rate')),
                ('bit', models.IntegerField(max_length=20, verbose_name='Bit')),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TermPaper.developer')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TermPaper.package')),
            ],
        ),
    ]
