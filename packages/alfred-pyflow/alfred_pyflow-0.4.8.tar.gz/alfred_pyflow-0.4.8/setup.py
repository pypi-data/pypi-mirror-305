# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyflow']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.30.0,<3.0.0', 'urllib3==2.2.1']

setup_kwargs = {
    'name': 'alfred-pyflow',
    'version': '0.4.8',
    'description': 'Minimal library for the development of Alfred Workflows.',
    'long_description': '# alfred-pyflow',
    'author': 'Fede Calendino',
    'author_email': 'fede@calendino.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/fedecalendino/alfred-pyflow',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
