# Generated by Django 4.2.4 on 2023-11-05 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_registermodel_age'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField()),
                ('course_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ExamModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_no', models.IntegerField()),
                ('exam_name', models.CharField(max_length=200)),
                ('total_number', models.IntegerField()),
                ('exam_marks', models.IntegerField()),
                ('min_marks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SectionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=200)),
                ('is_completed', models.BooleanField(default=False)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courseid', to='courses.coursesmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='username1', to='users.registermodel')),
            ],
        ),
        migrations.RemoveField(
            model_name='ooppythonmodel',
            name='basicpythonmodel_ptr',
        ),
        migrations.RemoveField(
            model_name='pythoncoursemodel',
            name='users',
        ),
        migrations.DeleteModel(
            name='BasicPythonModel',
        ),
        migrations.DeleteModel(
            name='OOPPythonModel',
        ),
        migrations.DeleteModel(
            name='PythonCourseModel',
        ),
        migrations.AddField(
            model_name='exammodel',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sectionid', to='courses.sectionmodel'),
        ),
        migrations.AddField(
            model_name='exammodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='username2', to='users.registermodel'),
        ),
    ]