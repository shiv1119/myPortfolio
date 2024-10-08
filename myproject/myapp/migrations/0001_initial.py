# Generated by Django 5.0.6 on 2024-06-25 05:02

import django.db.models.deletion
import phone_field.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=300)),
                ('mob_number', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('message', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SoftSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills_value', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills_value', models.TextField(max_length=500)),
                ('skills_logo', models.ImageField(upload_to='skills_logo/')),
            ],
        ),
        migrations.CreateModel(
            name='AuthorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_image/')),
                ('user_date_of_birth', models.DateField(blank=True, null=True)),
                ('user_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others'), ('P', 'Prefer Not To Say')], max_length=1)),
                ('github_username', models.CharField(blank=True, max_length=100, null=True)),
                ('portfolio_link', models.URLField(blank=True, null=True)),
                ('user_number', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31, null=True)),
                ('user_linkedin', models.URLField(blank=True, null=True)),
                ('user_x', models.URLField(blank=True, null=True)),
                ('user_github', models.URLField(blank=True, default='https://github.com/default')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
                ('soft_skills', models.ManyToManyField(related_name='profile', to='myapp.softskill')),
                ('technical_skills', models.ManyToManyField(related_name='profile', to='myapp.technicalskill')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('certificate_file', models.FileField(upload_to='certificates/')),
                ('certificate_link', models.URLField(blank=True, max_length=400, null=True)),
                ('certificate_provider_logo', models.ImageField(blank=True, null=True, upload_to='certificates_provider_logo/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('author_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificates', to='myapp.authorprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('project_image', models.ImageField(blank=True, null=True, upload_to='projects_images/')),
                ('github_link', models.URLField(max_length=600)),
                ('live_preview_link', models.URLField(max_length=600)),
                ('description', models.TextField(blank=True)),
                ('author_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='myapp.authorprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Repositories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo_name', models.CharField(max_length=400)),
                ('repo_link', models.URLField(blank=True)),
                ('author_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repositories', to='myapp.authorprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('content', models.TextField()),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('is_liked', models.BooleanField(default=False)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(related_name='posts', to='myapp.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_title', models.CharField(max_length=400)),
                ('degree', models.CharField(max_length=400)),
                ('field_of_study', models.CharField(max_length=400)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('grade', models.CharField(max_length=100)),
                ('activities_and_societies', models.TextField(blank=True, null=True)),
                ('author_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='myapp.authorprofile')),
                ('soft_skills', models.ManyToManyField(related_name='educations', to='myapp.softskill')),
                ('technical_skills', models.ManyToManyField(related_name='educations', to='myapp.technicalskill')),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_title', models.CharField(max_length=400)),
                ('company_name', models.CharField(max_length=250)),
                ('company_logo', models.ImageField(blank=True, null=True, upload_to='company_logo_image/')),
                ('company_portfolio_link', models.URLField(blank=True, null=True)),
                ('working_time', models.CharField(choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time'), ('Freelance', 'Freelance')], max_length=10)),
                ('working_type', models.CharField(choices=[('Remote', 'Remote'), ('On-Site', 'On-Site'), ('Hybrid', 'Hybrid')], max_length=7)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('activities_responsibilities', models.TextField(blank=True, null=True)),
                ('author_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_experiences', to='myapp.authorprofile')),
                ('soft_skills', models.ManyToManyField(related_name='work_experiences', to='myapp.softskill')),
                ('technical_skills', models.ManyToManyField(related_name='work_experiences', to='myapp.technicalskill')),
            ],
        ),
    ]
