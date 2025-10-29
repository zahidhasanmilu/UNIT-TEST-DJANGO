from django.contrib import admin
from documentation.models import Documentation, Languague, tags, Framwork


# Register your models here.
class DocumentationAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_by', 'language', 'display_framwork', 'display_tags', 'created_at', 'updated_at')
    readonly_fields = ('slug', 'created_at', 'updated_at')
    filter_horizontal = ('framwork', 'tags')  # nicer UI

    # Framwork ManyToMany দেখানোর জন্য
    def display_framwork(self, obj):
        return ", ".join([f.name for f in obj.framwork.all()])
    display_framwork.short_description = 'Frameworks'

    # Tags ManyToMany দেখানোর জন্য
    def display_tags(self, obj):
        return ", ".join([t.name for t in obj.tags.all()])
    display_tags.short_description = 'Tags'

class TagsAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    readonly_fields = ('slug', 'created_at', 'updated_at')  # make slug readonly


class LanguagueAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    readonly_fields = ('slug', 'created_at', 'updated_at')  # make slug readonly


class FramworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    readonly_fields = ('slug', 'created_at', 'updated_at')  # make slug readonly
    

admin.site.register(Documentation, DocumentationAdmin)
admin.site.register(tags, TagsAdmin)
admin.site.register(Languague, LanguagueAdmin)
admin.site.register(Framwork, FramworkAdmin)


