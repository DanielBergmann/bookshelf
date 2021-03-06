# Generated by Django 3.0.4 on 2020-04-08 10:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('author_name', models.CharField(max_length=200)),
                ('author_description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.UUIDField(default=uuid.UUID('79392b85-c020-451d-a913-ee0cc2e50078'), editable=False, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('book_title', models.CharField(max_length=100)),
                ('year', models.DateField(blank=True, null=True)),
                ('genre', models.CharField(blank=True, max_length=100, null=True)),
                ('lable', models.CharField(blank=True, max_length=50, null=True)),
                ('read_status', models.IntegerField(default=1)),
                ('who_has', models.CharField(default='YOU', max_length=50)),
                ('e_book', models.FileField(blank=True, null=True, upload_to='')),
                ('priority', models.IntegerField(default=0)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('book_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_shelf.Author')),
                ('who_ownes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_shelf.User')),
            ],
        ),
    ]
