from django import template
from ..models import Category
from django.shortcuts import get_list_or_404

register = template.Library()


@register.simple_tag
def title(data='وبلاگ جنگویی'):
	return data


@register.inclusion_tag('blog/partials/my_inclusion_tag.html')
def category_navbar():
	data = {
		'categores': get_list_or_404(Category, status=False)
		}
	return data