# Generated by Django 3.2.5 on 2021-07-05 20:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChallengeTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20, verbose_name='Challenge Tag')),
            ],
        ),
        migrations.CreateModel(
            name='ExperienceLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Your level of programming\n                            experience (ex: 2 years)', max_length=100, verbose_name='Level of Experience')),
            ],
        ),
        migrations.CreateModel(
            name='FactorTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20, verbose_name='Factor Tag')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('char_name', models.CharField(max_length=20, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this user', primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('which_submission', models.IntegerField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='challenge.user')),
            ],
        ),
        migrations.CreateModel(
            name='FactorSubmission',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this submission', primary_key=True, serialize=False)),
                ('challenge_tag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='challenge.challengetag')),
                ('factor_tag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='challenge.factortag')),
                ('submission', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='challenge.submission')),
            ],
        ),
    ]