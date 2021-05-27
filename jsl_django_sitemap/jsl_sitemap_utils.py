import importlib
import logging
from django.urls.resolvers import URLResolver,URLPattern
from django.conf import settings

from .default_settings import FETCH_URL_FROM, FETCH_URL_FROM_ALLOWED_PARAMS

logger = logging.getLogger(__name__)


def get_django_root_url_patterns():
	try:
		mod = importlib.import_module(settings.ROOT_URLCONF)
	except Exception as e:
		logger.error("Please ensure that Django settings has ROOT_URLCONF set properly")
		logger.error(e.args)
		return []
	return mod.urlpatterns


def filter_include_apps_in_url(all_urls, include_apps):
	modified_all_urls = []
	if 'ALL' in include_apps:
		return all_urls
	for url in all_urls:
		try:
			if url.app_name in include_apps:
				modified_all_urls.append(url)
		except:
			pass
	return modified_all_urls


def iterate_over_django_urls(all_urls, default_settings, return_url_list=set(),prefix=''):
	for url in all_urls:
		try:
			if url.url_patterns:
				if(isinstance(url, URLPattern)):
					prefix = ''
				elif (isinstance(url, URLResolver)):
					prefix = str(url.pattern)
				iterate_over_django_urls(url.url_patterns,default_settings, return_url_list,prefix=prefix)
		except:
			try:
				if "pattern" == default_settings.get(FETCH_URL_FROM).lower():
					pattern = str(url.pattern)
					if "^" == pattern[0]:
						pattern = pattern[1:]
					if "$" == pattern[len(pattern) - 1]:
						pattern = pattern[:len(pattern) - 1]
					return_url_list.add(prefix + pattern)
				else:
					return_url_list.add(prefix + url.name)
			except:
				pass

	return return_url_list


def get_django_urls(urlpatterns, default_settings=None):
	if default_settings is None:
		logger.error("Please set JSL_DJANGO_SITEMAP_SETTINGS in your Django settings")
		return []
	enable = default_settings.get('ENABLE')
	include_apps = default_settings.get('INCLUDE_APPS')
	if enable and include_apps is not None:

		all_urls = filter_include_apps_in_url(urlpatterns, include_apps)
		return list(iterate_over_django_urls(all_urls, default_settings))
	else:
		return []
