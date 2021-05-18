import importlib
import logging

from django.conf import settings

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


def iterate_over_django_urls(all_urls, return_url_list=set()):
	for url in all_urls:
		try:
			if url.url_patterns:
				iterate_over_django_urls(url.url_patterns, return_url_list)
		except:
			try:
				if 'sitemap' not in url.name:
					return_url_list.add(url.name)
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
		return list(iterate_over_django_urls(all_urls))
	else:
		return []
