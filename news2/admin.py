from django.contrib import admin
from . models import News2, Category2

# Register your models here.
# admin.site.register(News)


@admin.register(News2)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "reporter", "region"]
    list_filter = ["category", "region"]


admin.site.register(Category2)