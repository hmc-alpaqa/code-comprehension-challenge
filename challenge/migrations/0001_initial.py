# Generated by Django 3.2.5 on 2021-07-30 18:27

from django.db import migrations, models
import django.db.models.deletion


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
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_name', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubmissionSnapshot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_snapshot', models.CharField(max_length=2000, null=True, verbose_name='Input Snapshot')),
                ('time', models.IntegerField()),
                ('box', models.CharField(max_length=2, null=True, verbose_name='Which Textarea')),
                ('challenge_tag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='challenge.challengetag')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='challenge.user')),
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
            name='FinalQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers1', models.CharField(max_length=1000, null=True)),
                ('answers2', models.CharField(max_length=1000, null=True)),
                ('submission', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='challenge.submission')),
            ],
        ),
        migrations.CreateModel(
            name='FactorTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20, verbose_name='Factor Tag')),
                ('challenge_tag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='challenge.challengetag')),
            ],
        ),
        migrations.CreateModel(
            name='FactorSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=10, null=True)),
                ('response1', models.CharField(max_length=2000, null=True)),
                ('response2', models.CharField(max_length=2000, null=True)),
                ('challenge_tag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='challenge.challengetag')),
                ('factor_tag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='challenge.factortag')),
                ('submission', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='challenge.submission')),
            ],
        ),
    ]
