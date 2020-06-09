from django.contrib import admin
from .models import Star

# Register your models here.
@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
    def show_blogs(self,obj):
        return [i.title for i in obj.blogs.all()]
    show_blogs.short_description='收藏的博客'
    list_display=['name','user','brief','show_blogs','created_time','last_update_time','id']
    ordering=('id',)