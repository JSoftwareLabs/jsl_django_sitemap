import logging
from django.conf import settings

logger = logging.getLogger(__name__)
FETCH_URL_FROM = "FETCH_URL_FROM"
DEFAULT_FETCH_URL_FROM = "name"
ENABLE = "ENABLE"
INCLUDE_APPS = "INCLUDE_APPS"

FETCH_URL_FROM_ALLOWED_PARAMS = ["name", "pattern"]


def fetch_default_settings():
	if getattr(settings, 'JSL_DJANGO_SITEMAP_SETTINGS', None) is None:
		JSL_DJANGO_SITEMAP_SETTINGS = {
			ENABLE: True,
			FETCH_URL_FROM: DEFAULT_FETCH_URL_FROM,
			INCLUDE_APPS: ("ALL",)
		}
		return JSL_DJANGO_SITEMAP_SETTINGS
	else:
		ensure_correct_params(getattr(settings, 'JSL_DJANGO_SITEMAP_SETTINGS', None))
		return getattr(settings, 'JSL_DJANGO_SITEMAP_SETTINGS', None)


def ensure_correct_params(default_settings_v):
	if default_settings_v.get(FETCH_URL_FROM) not in FETCH_URL_FROM_ALLOWED_PARAMS:
		error_message = "FETCH_URL_FROM  should be one of " + str(FETCH_URL_FROM_ALLOWED_PARAMS)
		logger.error(error_message)
		raise Exception(error_message)
