# JSL Django Sitemap

[![Upload Python Package](https://github.com/JSoftwareLabs/jsl_django_sitemap/actions/workflows/python-publish.yml/badge.svg)](https://github.com/JSoftwareLabs/jsl_django_sitemap/actions/workflows/python-publish.yml)
---
A sitemap is an XML file on your website that tells search-engine crawlers or indexers how frequently your pages change and how “important” certain pages are in relation to other pages on your site. This information helps search engines index your site.

This Django sitemap framework library automates the creation of this XML file by letting you express this information in Python code. You have the ability to chnge and mention settings in your Django project's settings.py file. It is very convinent and easy to use library which detects the changes in your Django url configuration and reloads the new configuration making absolutely no manual interventions for your sitemap.

JSL Django Sitemap is a sitemap.xml creator for Django projects which iterates over all the url patterns in your main
Django project and creates a ready to use sitemap. The sitemap.xml is useful in crawlers such as Google, Bing, Yahoo. We
hope you like our app! Leave a star on our GitHub repository. Thanks!

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
	"FETCH_URL_FROM": "pattern",
	"INCLUDE_APPS": ("ALL",),
	"IGNORE_URL_PATTERNS": (".*/api/v1.*", )
}

```

# add django built in sitemap in the INSTALLED_APPS

```python
INSTALLED_APPS = [
	# ...
	'django.contrib.sitemaps',
]
```

> **_NOTE:_**
> 1. "ALL" means to include all the urls
> 2. If you want specific apps to be included in sitemap use below. Provide comma separated tuple containing your app name
> 3. "INCLUDE_APPS": ("myapp1","myapp2")
> 4. FETCH_URL_FROM: should be one value from the list ["name", "pattern"]
> 5. default for FETCH_URL_FROM is "pattern"
> 6. By default, if pattern is provided then "^" prefix and "$" suffix in urlpattern is removed.
> 7. "IGNORE_URL_PATTERNS": (".*/api/v1.*", ) This flag is used to ignore certain urls matching the provided tuple of patterns which are regex compatible
**_NOTE:_**
The sitemap application doesn't install any database tables. The only reason it needs to go into INSTALLED_APPS is so that the Loader() template loader can find the default templates.

## View generated sitemap:

Start the development server and visit http://127.0.0.1:8000/sitemap.xml

-----

## Current Releases

[1.2.4](https://github.com/JSoftwareLabs/jsl_django_sitemap/releases/tag/1.2.4)

## How to build and distribute using sdist setup.py and twine

```bash
python3 -m pip install --upgrade twine
python setup.py sdist
twine upload dist/*
```
