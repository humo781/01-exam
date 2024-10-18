from django.contrib import admin
from . import models

admin.site.register(models.Student)
admin.site.register(models.Group)
admin.site.register(models.Subject)
admin.site.register(models.Exam)
admin.site.register(models.StudentExam)
admin.site.register(models.Question)
admin.site.register(models.Option)
