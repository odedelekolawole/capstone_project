from django.contrib import admin
from . models import News, Category

# Register your models here.
# admin.site.register(News)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "reporter", "region"]
    list_filter = ["category", "region"]


admin.site.register(Category)


    