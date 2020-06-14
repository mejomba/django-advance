from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext
from .models import Article, Category

def make_published(modeladmin, request, queryset):
	updated = queryset.update(status='P')
	modeladmin.message_user(request, ngettext(
			'%d مقاله با موفقیت منتشر شد.',
			'%d مقاله با موفقیت منتشر شدند.',
			updated,
		) % updated, messages.SUCCESS)
make_published.short_description = 'انتشار مقاله'

def make_draft(modeladmin, request, queryset):
	updated = queryset.update(status='D')
	modeladmin.message_user(request, ngettext(
			'%d مقاله با موفقیت پیشنویس شد.',
			'%d مقاله با موفقیت پیشنویس شدند.',
			updated,
		) % updated, messages.SUCCESS)
make_draft.short_description = 'پیشنویس کردن'


class CategoryAdmin(admin.ModelAdmin):
	list_display	= ('title','slug','jupdated', 'parent', 'status', 'position')
	list_filter		= (['status'])
	search_fields	= ('title', 'slug')
	prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
	list_display	= ('title','slug', 'thumbnail_display', 'jpublish', 'jupdated', 'status', 'category_str')
	list_filter		= ('publish', 'status')
	search_fields	= ('title', 'slug', 'description')
	prepopulated_fields = {'slug': ('title',)}
	ordering		= ['-status', 'publish']
	actions			= [make_published, make_draft]

	def category_str(self, obj):
		return '، '.join([category.title for category in obj.category.all() if not category.status])
	category_str.short_description = 'دسته بندی ها'

admin.site.register(Article, ArticleAdmin)