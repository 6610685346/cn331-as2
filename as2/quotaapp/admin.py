from django.contrib import admin
from .models import Subject, Course, Student
# Register your models here.


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("subject_id", "subject_name")


class CourseAdmin(admin.ModelAdmin):
    list_display = ("course", "semester", "year", "seat", "status")


class StudentAdmin(admin.ModelAdmin):
    list_display = ("student",)
    filter_horizontal = ("applys",)


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
