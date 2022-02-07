from django.contrib import admin
from . import models
@admin.register(models.McaNotice)
class McaNoticeAdmin(admin.ModelAdmin):
    list_display=['id','title','file']
@admin.register(models.StatisticNotice)
class StatisticNoticeAdmin(admin.ModelAdmin):
    list_display=['id','title','file']
@admin.register(models.McaAdmission)
class McaAdmissionAdmin(admin.ModelAdmin):
    list_display=['id','title','file']
@admin.register(models.StatisticAdmission)
class StatisticAdmissionAdmin(admin.ModelAdmin):
    list_display=['id','title','file']
@admin.register(models.McaResult)
class McaResultAdmin(admin.ModelAdmin):
    list_display=['id','title','file']
@admin.register(models.StatisticResult)
class StatisticResultAdmin(admin.ModelAdmin):
    list_display=['id','title','file']
@admin.register(models.McaCourse)
class McaCourseAdmin(admin.ModelAdmin):
    list_display=['file',]
@admin.register(models.StatisticCourse)
class StatisticCourseAdmin(admin.ModelAdmin):
    list_display=['file',]
@admin.register(models.LatestDept)
class LatestDeptAdmin(admin.ModelAdmin):
    list_display=['id','title','file']
@admin.register(models.Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display=['id','img']
@admin.register(models.Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display=['id','qualification']
@admin.register(models.McaFaculty)
class McaFacultyAdmin(admin.ModelAdmin):
    list_display=['id','name','experience','img']
@admin.register(models.McaSubject)
class McaStudentAdmin(admin.ModelAdmin):
    list_display=['id','subject']
@admin.register(models.StatisticsSubject)
class StatisticsStudentAdmin(admin.ModelAdmin):
    list_display=['id','subject']
@admin.register(models.StatisticsFaculty)
class StatisticsFacultyAdmin(admin.ModelAdmin):
    list_display=['id','name','administrative_post','experience','img']
@admin.register(models.McaSemister1)
class McaSemister1Admin(admin.ModelAdmin):
    list_display=['id','title','file']
@admin.register(models.McaSemister2)
class McaSemister2Admin(admin.ModelAdmin):
    list_display=['id','title','file']
@admin.register(models.McaSemister3)
class McaSemister3Admin(admin.ModelAdmin):
    list_display=['id','title','file']
@admin.register(models.McaSemister4)
class McaSemister4Admin(admin.ModelAdmin):
    list_display=['id','title','file']
@admin.register(models.McaSemister5)
class McaSemister5Admin(admin.ModelAdmin):
    list_display=['id','title','file']
@admin.register(models.McaSemister6)
class McaSemister6Admin(admin.ModelAdmin):
    list_display=['id','title','file']
@admin.register(models.StatisticSemister1)
class StatisticSemister1Admin(admin.ModelAdmin):
    list_display=['id','title','file']
@admin.register(models.StatisticSemister2)
class StatisticSemister2Admin(admin.ModelAdmin):
    list_display=['id','title','file']
@admin.register(models.StatisticSemister3)
class StatisticSemister3Admin(admin.ModelAdmin):
    list_display=['id','title','file']

@admin.register(models.StatisticSemister4)
class StatisticSemister4Admin(admin.ModelAdmin):
    list_display=['id','title','file']

@admin.register(models.StatisticSemister5)
class StatisticSemister5Admin(admin.ModelAdmin):
    list_display=['id','title','file']

@admin.register(models.StatisticSemister6)
class StatisticSemister6Admin(admin.ModelAdmin):
    list_display=['id','title','file']

@admin.register(models.Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display=['id','title','img']

@admin.register(models.StudentBlog)
class StudentBlogAdmin(admin.ModelAdmin):
    list_display=['id','upload_date','title','img','content']

@admin.register(models.McaEbook)
class McaEbookAdmin(admin.ModelAdmin):
    list_display=['id','title','writer','file']
@admin.register(models.StatisticEbook)
class StatisticEbookAdmin(admin.ModelAdmin):
    list_display=['id','title','writer','file']
@admin.register(models.ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display=['id','name','email','query','file']










