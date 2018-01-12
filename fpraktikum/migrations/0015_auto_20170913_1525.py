# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 15:25


import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('fpraktikum', '0014_auto_20170913_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fpinstitute',
            name='places',
            field=models.IntegerField(blank=True, default=0, verbose_name='places'),
        ),
        migrations.AlterField(
            model_name='fpinstitute',
            name='registration',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE,
                                    related_name='institutes', to='fpraktikum.FpRegistration',
                                    verbose_name='registration'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fpinstitute',
            name='semester_half',
            field=models.IntegerField(blank=True, choices=[(1, '1.'), (2, '2.'), (3, 'both')],
                                      verbose_name='semester half'),
        ),
        migrations.AlterField(
            model_name='fpregistration',
            name='end_date',
            field=models.DateTimeField(verbose_name='enddate of registration'),
        ),
        migrations.AlterField(
            model_name='fpregistration',
            name='start_date',
            field=models.DateTimeField(verbose_name='startdate of registration'),
        ),
        migrations.AlterField(
            model_name='fpuserpartner',
            name='registrant',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='partner',
                                       to='fpraktikum.FpUserRegistrant', verbose_name='registrant'),
        ),
        migrations.AlterField(
            model_name='fpuserpartner',
            name='user_email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='user email'),
        ),
        migrations.AlterField(
            model_name='fpuserpartner',
            name='user_firstname',
            field=models.CharField(blank=True, max_length=100, verbose_name='user firstname'),
        ),
        migrations.AlterField(
            model_name='fpuserpartner',
            name='user_lastname',
            field=models.CharField(blank=True, max_length=100, verbose_name='user lastname'),
        ),
        migrations.AlterField(
            model_name='fpuserpartner',
            name='user_login',
            field=models.CharField(blank=True, max_length=100, verbose_name='s number / login'),
        ),
        migrations.AlterField(
            model_name='fpuserpartner',
            name='user_matrikel',
            field=models.CharField(blank=True, max_length=100, verbose_name='Matrikelnumber'),
        ),
        migrations.AlterField(
            model_name='fpuserregistrant',
            name='user_email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='user email'),
        ),
        migrations.AlterField(
            model_name='fpuserregistrant',
            name='user_firstname',
            field=models.CharField(blank=True, max_length=100, verbose_name='user firstname'),
        ),
        migrations.AlterField(
            model_name='fpuserregistrant',
            name='user_lastname',
            field=models.CharField(blank=True, max_length=100, verbose_name='user lastname'),
        ),
        migrations.AlterField(
            model_name='fpuserregistrant',
            name='user_login',
            field=models.CharField(blank=True, max_length=100, verbose_name='s number / login'),
        ),
        migrations.AlterField(
            model_name='fpuserregistrant',
            name='user_matrikel',
            field=models.CharField(blank=True, max_length=100, verbose_name='Matrikelnumber'),
        ),
        migrations.AlterField(
            model_name='fpwaitlist',
            name='user_email',
            field=models.EmailField(max_length=254, verbose_name='user email'),
        ),
        migrations.AlterField(
            model_name='fpwaitlist',
            name='user_firstname',
            field=models.CharField(max_length=100, verbose_name='user firstname'),
        ),
        migrations.AlterField(
            model_name='fpwaitlist',
            name='user_lastname',
            field=models.CharField(max_length=100, verbose_name='user lastname'),
        ),
        migrations.AlterField(
            model_name='fpwaitlist',
            name='user_login',
            field=models.CharField(blank=True, max_length=100, verbose_name='s number / login'),
        ),
        migrations.AlterField(
            model_name='fpwaitlist',
            name='user_matrikel',
            field=models.CharField(blank=True, max_length=100, verbose_name='Matrikelnummer'),
        ),
    ]
