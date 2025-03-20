from django.contrib import admin
from .models import Blog
from django.db import models
from django.utils.safestring import mark_safe
from django.forms import Textarea
import markdown

# Register your models here.


# For Main ADMIN Panel Change
admin.site.site_header = "Blogging"
admin.site.site_title = "Blogging Portal"
admin.site.index_title = "Blogging Panel"  


# For the Blog app changes

class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active',)
    list_editable = ('is_active',)

    def content_preview(self, obj):
        # Convert Markdown to HTML using the markdown library
        html_content = markdown.markdown(obj.content)
        # Use mark_safe to render HTML content in the admin panel
        return mark_safe(html_content)

    content_preview.short_description = 'Markdown Preview'
    readonly_fields = ['content_preview']
    
    # Optional: Add the preview field to the fields in the form
    fieldsets = (
        (None, {
            'fields': ('name', 'short_desc','image','slug','content', 'content_preview')
        }),
    )



admin.site.register(Blog, BlogAdmin)