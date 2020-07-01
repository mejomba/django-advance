from django.db import models
from django.urls import reverse
from accounts.models import User
from django.utils import timezone
from django.utils.html import format_html
from extension.utils import to_jalali

class ArticleManager(models.Manager):
	def published(self):
		return self.filter(status='P')


class CategoryManager(models.Manager):
	def active(self):
		return self.filter(status=False)


class Category(models.Model):
	parent 		= models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL ,related_name='parent_related_name', verbose_name='دسته مادر')
	title 		= models.CharField(max_length=200, verbose_name='عنوان دسته')
	slug		= models.SlugField(max_length=100, unique=True, verbose_name='نام اختصاصی')
	updated 	= models.DateTimeField(auto_now=True, verbose_name='آخرین بروز زسانی')
	position 	= models.PositiveIntegerField(unique=True, verbose_name='جایگاه')
	status 		= models.BooleanField(default=False, verbose_name='عدم نمایش')


	class Meta:
		verbose_name = 'دسته بندی'
		verbose_name_plural = 'دسته بندی ها'
		ordering = ['parent__id', 'position']

	def __str__(self):
		return self.title

	def jupdated(self):
		return to_jalali(self.updated)
	jupdated.short_description = 'آخرین به روز رسانی'

	objects = CategoryManager()


class Article(models.Model):
	STATUS_CHOICES = (
			('D', 'پیش نویس'),
			('P', 'منتشر شده'),
			('I', 'درحال بررسی'),
			('B', 'برگشت داده شده'),
		)
	author 		= models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name='نویسنده', related_name='related_name')
	title 		= models.CharField(max_length=200, verbose_name='عنوان')
	slug		= models.SlugField(max_length=100, unique=True, verbose_name='نام اختصاصی')
	description = models.TextField(verbose_name='توضیحات')
	thumbnail	= models.ImageField(upload_to='images',verbose_name='تصویر')
	publish		= models.DateTimeField(default=timezone.now, verbose_name='اراعه شده')
	created		= models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده')
	updated 	= models.DateTimeField(auto_now=True, verbose_name='آخرین بروز زسانی')
	status 		= models.CharField(choices=STATUS_CHOICES, max_length=1, verbose_name='وضعیت')
	category 	= models.ManyToManyField('Category', verbose_name='دسته بندی', related_name='related_name', null=True, blank=True)
	optional_description = models.TextField(verbose_name='توضیحات اختیاری', null=True, blank=True)
	class Meta:
		verbose_name = 'مقاله'
		verbose_name_plural = 'مقاله'


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("accounts:account")

	def jpublish(self):
		return to_jalali(self.publish)
	jpublish.short_description = 'تاریخ انتشار'

	def jupdated(self):
		return to_jalali(self.updated)
	jupdated.short_description = 'آخرین به روز رسانی'

	# def cat_publish(self):
	# 	return self.category.filter(status=False)

	def thumbnail_display(self):
		return format_html('<img width=128 src={}>'.format(self.thumbnail.url))
	thumbnail_display.short_description = 'تصویر'

	# def category_str(self):
	# 	return '، '.join([category.title for category in self.category.all() if not category.status])
	# category_str.short_description = 'دسته بندی ها'

	def category_str(self):
		return '، '.join([category.title for category in self.category.active()])
	category_str.short_description = 'دسته بندی ها'

	objects = ArticleManager()