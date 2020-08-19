from django.contrib import admin
from .models import Post, Tag, Comment

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag,TagAdmin)