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
		'categores': get_list_or_404(Category, status=False),
		}
	return data


@register.inclusion_tag('registration/partials/sidebar-item.html')
def sidebar_item(request, link_name, icon, content, span_title, span_class):
	data = {
		'request': request,
		'link': '{}:{}'.format(request.resolver_match.app_name, link_name),
		'css_class': link_name,
		'icon': icon,
		'content': content,
		'span_title': span_title,
		'span_class': span_class,
	}
	return data