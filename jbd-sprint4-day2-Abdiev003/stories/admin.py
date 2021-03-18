from django.contrib import admin
from stories.models import (
    Recipe,
    Contact,
    Category,
    Tag,
    Comment
)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'parent_comment', 'created_at')


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'order', 'is_published', 'created_at')
    list_filter = ('is_published', 'author__username', 'category__title')
    search_fields = ('title', 'category__title', )
    fieldsets = (
        ('Melumatlar', {
            'description': 'bu saheler melumat xarakterlidir',
            # 'classes': ('collapse',),
            'fields': ('title', 'slug', 'short_description', 'description', 'image',)
        }),
        ('relations', {
            'description': 'relations desc',
            'classes': ('collapse',),
            'fields': ('category', 'author', 'tags',)
        }),
        ('moderation', {
            'description': 'moderation desc',
            'classes': ('collapse',),
            'fields': ('is_published',)
        }),
    )


class RecipeInlineAdmin(admin.TabularInline):
    model = Recipe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (RecipeInlineAdmin, )


admin.site.register(Recipe, RecipeAdmin)
admin.site.register([Contact, Tag])

