from django.conf import settings


def fetch_default_settings():
	if getattr(settings, 'JSL_DJANGO_SITEMAP_SETTINGS',None) is None:
		JSL_DJANGO_SITEMAP_SETTINGS = {
			"ENABLE": True,
			"INCLUDE_APPS": ("ALL",)
		}
		return JSL_DJANGO_SITEMAP_SETTINGS
	else:
		return getattr(settings, 'JSL_DJANGO_SITEMAP_SETTINGS', None)
