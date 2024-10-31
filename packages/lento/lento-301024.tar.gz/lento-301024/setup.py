from setuptools import setup


setup(
	name = 'lento',
	# version = '0.0.5',
	description = 'Programmatically generate Lilypond scores, with ease and elegance of pure Python ',
	author = 'Amir Teymuri',
	author_email = 'amiratwork22@gmail.com',
	packages = ['lento'],
    package_dir = {'lento': 'src/lento'},
    url = '',
    python_requires = ">=3.5",
)

