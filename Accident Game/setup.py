from setuptools import setup

def get_description():
	with open("README.md", 'r') as f:
		return f.read()

setup(name = "accidentgame",
	version = "0.1",
	description = get_description(),
	url = "https://github.com/BensonMuriithi/python/tree/master/accident_game",
	author = "Benson Muriithi",
	author_email = "mwngmuriithi@gmail.com",
	packages = ["accidentgame"],
	zip_safe = False,
)