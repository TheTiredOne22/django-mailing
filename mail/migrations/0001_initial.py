# Generated by Django 4.2.10 on 2024-02-11 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('attachments', models.FileField(blank=True, upload_to='', verbose_name='Attachment')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, default=uuid.uuid4, editable=False, max_length=16, unique=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('is_read', models.BooleanField(default=False)),
                ('is_deleted_by_sender', models.BooleanField(default=False)),
                ('is_deleted_by_recipient', models.BooleanField(default=False)),
                ('is_starred_by_sender', models.BooleanField(default=False)),
                ('is_starred_by_recipient', models.BooleanField(default=False)),
                ('parent_email', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='mail.email')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_emails', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_emails', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mail.email')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
