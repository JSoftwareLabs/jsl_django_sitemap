# JSL Django Sitemap

JSL Django Sitemap is a Django utility which iterates over all the url patterns in your main Django project and creates a
ready to use sitemap. The sitemap.xml is useful in crawlers such as Google, Bing, Yahoo. We hope you like our app! Leave
a star on our GitHub repository. Thanks!

# Our Home page [JSoftwareLabs.com](https://www.jsoftwarelabs.com/)

## Installation

You can install the JSL Django Sitemap from [PyPI](https://pypi.org/project/jsl-django-sitemap/):

    pip install jsl-django-sitemap

---

# Example Usage

Add necessary imports
---

```python
from jsl_django_sitemap.views import sitemaps
from django.contrib.sitemaps.views import sitemap
from django.urls import path

```

In your main django project urls.py file add below in urlpatterns
---

```python

path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
	 name='django.contrib.sitemaps.views.sitemap'),
```

In your main settings.py file add below
---

```python

JSL_DJANGO_SITEMAP_SETTINGS = {
	"ENABLE": True,
	"INCLUDE_APPS": ("ALL",)
}

```

# add django built in sitemap in the INSTALLED_APPS
```python
INSTALLED_APPS = [
	#...
	'django.contrib.sitemaps',
]
```

> **_NOTE:_**
> 1. "ALL" means to include all the urls
> 2. If you want specific apps to be included in sitemap use below. Provide comma separated tuple containing your app name
> 3. "INCLUDE_APPS": ("myapp1","myapp2")



## View generated sitemap:

Start the development server and visit http://127.0.0.1:8000/sitemap.xml

-----

## Current Releases

[1.0.7](https://github.com/JSoftwareLabs/jsl_django_sitemap/releases/tag/1.0.7)

