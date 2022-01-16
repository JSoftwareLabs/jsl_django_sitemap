from os import path

import setuptools
from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
	long_description = f.read()

setup(
	name='jsl_django_sitemap',  # How you named your package folder (MyLib)
	packages=setuptools.find_packages(),  # Chose the same as "name"
	version='1.2.0',  # Start with a small number and increase it with every change you make
	license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
	description='JSL Django Sitemap is a Django utility which iterates over all the url patterns in your main Django project and creates a ready to use sitemap. The sitemap.xml is useful in crawlers such as Google, Bing, Yahoo. We hope you like our app! Leave a star on our GitHub repository. Thanks!',
	# Give a short description about your library
	long_description=long_description,
	long_description_content_type='text/markdown',
	author='JSoftwareLabs.com',  # Type in your name
	author_email='info@jsoftwarelabs.com',  # Type in your E-Mail
	url='https://github.com/JSoftwareLabs/jsl_django_sitemap',
	# Provide either the link to your github or to your website
	download_url='https://github.com/JSoftwareLabs/jsl_django_sitemap/archive/refs/tags/1.2.0.tar.gz',
	# I explain this later on
	keywords=['Django sitemap', 'JSoftwareLabs', 'sitemap.xml', 'Django automated sitemaps'],
	# Keywords that define your package best
	install_requires=[  # I get to this in a second
		'Django>=2.2',
	],
	include_package_data=True,
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		# Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
		'Intended Audience :: Developers',  # Define that your audience are developers
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: Apache Software License',  # Again, pick a license
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
	],
)
