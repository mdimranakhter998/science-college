# Generated by Django 4.0.1 on 2022-02-07 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mca', '0002_alter_mcaebook_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='img',
            field=models.ImageField(max_length=200, upload_to='admin/carousel/'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='file',
            field=models.FileField(upload_to='user/contactus/'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='img',
            field=models.ImageField(max_length=200, upload_to='admin/StatisticdeptGallery/'),
        ),
        migrations.AlterField(
            model_name='latestdept',
            name='file',
            field=models.FileField(upload_to='admin/lastestdeptupdate/'),
        ),
        migrations.AlterField(
            model_name='mcaadmission',
            name='file',
            field=models.FileField(upload_to='admin/mcaadmission/'),
        ),
        migrations.AlterField(
            model_name='mcacourse',
            name='file',
            field=models.FileField(upload_to='pdf/mcacourse/'),
        ),
        migrations.AlterField(
            model_name='mcaebook',
            name='file',
            field=models.FileField(max_length=200, upload_to='admin/mcaebook/'),
        ),
        migrations.AlterField(
            model_name='mcafaculty',
            name='img',
            field=models.ImageField(max_length=200, upload_to='admin/mcafaculty/'),
        ),
        migrations.AlterField(
            model_name='mcanotice',
            name='file',
            field=models.FileField(upload_to='admin/mcanotice/'),
        ),
        migrations.AlterField(
            model_name='mcaresult',
            name='file',
            field=models.FileField(upload_to='admin/mcaresults/'),
        ),
        migrations.AlterField(
            model_name='mcasemister1',
            name='file',
            field=models.FileField(max_length=200, upload_to='admin/mcaquestions/'),
        ),
        migrations.AlterField(
            model_name='mcasemister2',
            name='file',
            field=models.FileField(max_length=200, upload_to='admin/mcaquestions/'),
        ),
        migrations.AlterField(
            model_name='mcasemister3',
            name='file',
            field=models.FileField(max_length=200, upload_to='admin/mcaquestions/'),
        ),
        migrations.AlterField(
            model_name='mcasemister4',
            name='file',
            field=models.FileField(max_length=200, upload_to='admin/mcaquestions/'),
        ),
        migrations.AlterField(
            model_name='mcasemister5',
            name='file',
            field=models.FileField(max_length=200, upload_to='admin/mcaquestions/'),
        ),
        migrations.AlterField(
            model_name='mcasemister6',
            name='file',
            field=models.FileField(max_length=200, upload_to='admin/mcaquestions/'),
        ),
        migrations.AlterField(
            model_name='statisticadmission',
            name='file',
            field=models.FileField(upload_to='admin/statisticadmission/'),
        ),
        migrations.AlterField(
            model_name='statisticcourse',
            name='file',
            field=models.FileField(upload_to='pdf/statisticcourse/'),
        ),
        migrations.AlterField(
            model_name='statisticebook',
            name='file',
            field=models.FileField(max_length=200, upload_to='admin/statisticebook/'),
        ),
        migrations.AlterField(
            model_name='statisticnotice',
            name='file',
            field=models.FileField(upload_to='admin/statisticnotice/'),
        ),
        migrations.AlterField(
            model_name='statisticresult',
            name='file',
            field=models.FileField(upload_to='admin/statisticresults/'),
        ),
        migrations.AlterField(
            model_name='statisticsemister1',
            name='file',
            field=models.FileField(max_length=200, upload_to='admin/statisticquestions/'),
        ),
        migrations.AlterField(
            model_name='statisticsemister2',
            name='file',
            field=models.FileField(max_length=200, upload_to='admin/statisticquestions/'),
        ),
        migrations.AlterField(
            model_name='statisticsemister3',
            name='file',
            field=models.FileField(max_length=200, upload_to='admin/statisticquestions/'),
        ),
        migrations.AlterField(
            model_name='statisticsemister4',
            name='file',
            field=models.FileField(max_length=200, upload_to='admin/statisticquestions/'),
        ),
        migrations.AlterField(
            model_name='statisticsemister5',
            name='file',
            field=models.FileField(max_length=200, upload_to='admin/statisticquestions/'),
        ),
        migrations.AlterField(
            model_name='statisticsemister6',
            name='file',
            field=models.FileField(max_length=200, upload_to='admin/statisticquestions/'),
        ),
        migrations.AlterField(
            model_name='statisticsfaculty',
            name='img',
            field=models.ImageField(max_length=200, upload_to='admin/mcafaculty/'),
        ),
        migrations.AlterField(
            model_name='studentblog',
            name='img',
            field=models.ImageField(max_length=200, upload_to='admin/studentblogGallery/'),
        ),
    ]