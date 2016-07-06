try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	"description": "Lexicon determines the types of words entered as input",
	"author": "Benson Muriithi",
	"url": "No Current website",
	"download_url": " https://github.com/BensonMuriithi/lexicon"
	"author_email": "mwngmuriithi@gmail.com",
	"version": "0.1",
	"install_requires": ["nose"],
	"packages": ["Lexicon", "tests"],
	"scripts": [],
	"long_description": open("README").read()
	"name": "Input Lexicon"
}

setup(**config)