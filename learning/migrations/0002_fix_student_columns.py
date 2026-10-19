from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=100, default='Unknown'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=100, default='Unknown'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.CharField(max_length=100, default='Not Assigned'),
            preserve_default=False,
        ),
    ]