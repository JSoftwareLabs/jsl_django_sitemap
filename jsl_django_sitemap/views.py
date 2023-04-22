# from django.conf import settings
import re

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .default_settings import fetch_default_settings
from .jsl_sitemap_utils import get_django_urls, get_django_root_url_patterns


class StaticViewSitemap(Sitemap):
	priority = 0.5
	changefreq = 'daily'
	urlpatterns = []
	protocol = 'https'

	def items(self):
		self.urlpatterns = get_django_root_url_patterns()
		i = get_django_urls(self.urlpatterns, default_settings=fetch_default_settings())
		s = fetch_default_settings()
		filter_expression = lambda p, x: any(re.search(a, x) for a in p)
		i = [x for x in i if not filter_expression(s.get('IGNORE_URL_PATTERNS'), x)]
		return i
	# for p in s.IGNORE_URL_PATTERNS:
	# 	i = list(filter(filter_expression(p,), i))

	def location(self, item):
		try:
			return reverse(item)
		except:
			return "/" + item


sitemaps = {
	'static': StaticViewSitemap,
}
