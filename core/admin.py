from django.contrib import admin
from .models import SubjectModel
# Register your models here.


@admin.register(SubjectModel)
class SubjectModelAdmin(admin.ModelAdmin):
    list_display=['id','subject_name','subject_topic']