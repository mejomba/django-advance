from django.db import models
from django.utils import timezone
from extension.utils import to_jalali


class Category(models.Model):
	title 		= models.CharField(max_length=200, verbose_name='عنوان دسته')
	slug		= models.SlugField(max_length=100, unique=True, verbose_name='نام اختصاصی')
	updated 	= models.DateTimeField(auto_now=True, verbose_name='آخرین بروز زسانی')
	position 	= models.PositiveIntegerField(unique=True, verbose_name='جایگاه')
	status 		= models.BooleanField(default=False, verbose_name='عدم نمایش')


	class Meta:
		verbose_name = 'دسته بندی'
		verbose_name_plural = 'دسته بندی ها'
		ordering = ['position']

	def __str__(self):
		return self.title

	def jupdated(self):
		return to_jalali(self.updated)
	jupdated.short_description = 'آخرین به روز رسانی'


class Article(models.Model):
	STATUS_CHOICES = (
			('D', 'پیش نویس'),
			('P', 'منتشر شده'),
		)
	title 		= models.CharField(max_length=200, verbose_name='عنوان')
	slug		= models.SlugField(max_length=100, unique=True, verbose_name='نام اختصاصی')
	description = models.TextField(verbose_name='توضیحات')
	thumbnail	= models.ImageField(upload_to='images',verbose_name='تصویر')
	publish		= models.DateTimeField(default=timezone.now, verbose_name='اراعه شده')
	created		= models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده')
	updated 	= models.DateTimeField(auto_now=True, verbose_name='آخرین بروز زسانی')
	status 		= models.CharField(choices=STATUS_CHOICES, max_length=1, verbose_name='وضعیت')
	category 	= models.ManyToManyField('Category', verbose_name='دسته بندی', related_name='related_name')
	class Meta:
		verbose_name = 'مقاله'
		verbose_name_plural = 'مقاله'


	def __str__(self):
		return self.title

	def jpublish(self):
		return to_jalali(self.publish)
	jpublish.short_description = 'تاریخ انتشار'

	def jupdated(self):
		return to_jalali(self.updated)
	jupdated.short_description = 'آخرین به روز رسانی'

	def cat_publish(self):
		return self.category.filter(status=False)