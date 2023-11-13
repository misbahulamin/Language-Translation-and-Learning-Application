

from django.contrib import admin

# Register your models here.
# from models import CoursesModel, ExamModel, SectionModel

from .import models


admin.site.register(models.CoursesModel)
admin.site.register(models.ExamModel)
admin.site.register(models.SectionModel)

