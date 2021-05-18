# from django.conf import settings
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .default_settings import fetch_default_settings
from .jsl_sitemap_utils import get_django_urls, get_django_root_url_patterns


class StaticViewSitemap(Sitemap):
	priority = 0.5
	changefreq = 'daily'
	urlpatterns = []

	def items(self):
		self.urlpatterns = get_django_root_url_patterns()
		return get_django_urls(self.urlpatterns, default_settings=fetch_default_settings())

	def location(self, item):
		try:
			return reverse(item)
		except:
			return "/" + item


sitemaps = {
	'static': StaticViewSitemap,
}
