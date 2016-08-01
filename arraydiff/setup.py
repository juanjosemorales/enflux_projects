try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A project to calculate differences in lists',
    'author': 'Juan Jose Morales',
    'url': '',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['argparse'],
    'packages': ['array_diff'],
    'name': 'enflux_arraydiff'
}

setup(**config)