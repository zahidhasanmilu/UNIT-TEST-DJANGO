from django.contrib import admin
from app_unit_test.models import Category, Blog

# Register your models here.
#ListDisplay
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'updated_at')
    

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'category', 'created_at', 'updated_at')
    readonly_fields = ('slug',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)