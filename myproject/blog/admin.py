from django.contrib import admin
from .models import Article, Category


class CategoryAdmin(admin.ModelAdmin):
	list_display	= ('title','slug','jupdated','status', 'position')
	list_filter		= (['status'])
	search_fields	= ('title', 'slug')
	prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
	list_display	= ('title','slug','jpublish','jupdated','status', 'category_str')
	list_filter		= ('publish', 'status')
	search_fields	= ('title', 'slug', 'description')
	prepopulated_fields = {'slug': ('title',)}
	ordering		= ['-status', 'publish']

	def category_str(self, obj):
		return '، '.join([category.title for category in obj.category.all() if not category.status])
	category_str.short_description = 'دسته بندی ها'

admin.site.register(Article, ArticleAdmin)