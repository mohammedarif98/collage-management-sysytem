from django.contrib import admin
from AppCollage.models import CourseModel,TeacherModel
# Register your models here.


@admin.register(CourseModel)
class CourseDetailAdmin(admin.ModelAdmin):
    list_display=('id','Course_Name','Course_Fees')

@admin.register(TeacherModel)
class TeacherDetailAdmin(admin.ModelAdmin):
    list_display=('id','Teacher_Address','Teacher_Gender','Teacher_Age','Teacher_Photo')

