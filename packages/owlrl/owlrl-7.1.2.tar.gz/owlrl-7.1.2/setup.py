# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['owlrl']

package_data = \
{'': ['*']}

install_requires = \
['rdflib>=7.1.1']

setup_kwargs = {
    'name': 'owlrl',
    'version': '7.1.2',
    'description': 'A simple implementation of the OWL2 RL Profile, as well as a basic RDFS inference, on top of RDFLib. Based mechanical forward chaining.',
    'long_description': "|Original Author DOI| |PyPI badge|\n\n|OWL-RL Logo|\n\n.. |Original Author DOI| image:: https://zenodo.org/badge/9385/RDFLib/OWL-RL.svg\n    :target: http://dx.doi.org/10.5281/zenodo.14543\n\n.. |PyPI badge| image:: https://badge.fury.io/py/owlrl.svg\n    :target: https://badge.fury.io/py/owlrl\n\n.. |OWL-RL Logo| image:: https://raw.githubusercontent.com/RDFLib/OWL-RL/master/OWL-RL.png\n    :width: 250\n    :target: http://owl-rl.readthedocs.io/\n\n\nOWL-RL\n======\n\nA simple implementation of the OWL2 RL Profile, as well as a basic RDFS inference, on top of RDFLib. Based mechanical forward chaining. The distribution contains:\n\n**OWL-RL**: the Python library. You should copy the directory somewhere into your :code:`PYTHONPATH`. Alternatively, you can also run the :code:`python setup.py install` script in the directory.\n\n* :code:`scripts/RDFConvertService`: can be used as a CGI script to invoke the library. It may have to be adapted to the local server setup.\n\n* :code:`scripts/owlrl`: script that can be run locally on to transform a file into RDF (on the standard output). Run the script with :code:`-h` to get the available flags.\n\nThe package requires Python version 3.5 or higher; it depends on `RDFLib`_; version 4.2.2 or higher is required. If you need the python 2.7.x compatible version, see the @/py2 branch in this repository.\n\n.. _RDFLib: https://github.com/RDFLib\n\nFor the details on RDFS, see the `RDF Semantics Specification`_; for OWL 2 RL, see the `OWL 2 Profile specification`_.\n\n.. _RDF Semantics Specification: http://www.w3.org/TR/rdf11-mt/\n.. _OWL 2 Profile specification: http://www.w3.org/TR/owl2-profiles/#Reasoning_in_OWL_2_RL_and_RDF_Graphs_using_Rules\n\nView the **OWL-RL documentation** online: http://owl-rl.readthedocs.io/\n\nTo view the changelog for this software library, see `CHANGELOG.rst <CHANGELOG.rst>`_.\n\nThis software is released under the W3C© SOFTWARE NOTICE AND LICENSE. See `LICENSE.txt <LICENSE.txt>`_.\n\n\nRelease Procedure\n-----------------\n\n* update all the version numbers\n* remove the current dist dir\n* build the new distribution\n* test the metadata rendering\n* test push it to PyPI\n* actually push it to PyPI\n\n::\n\n    rm -vf dist/*\n    poetry build\n    bsdtar -xvf dist/owlrl-*.whl -O '*/METADATA' | view -\n    bsdtar -xvf dist/owlrl-*.tar.gz -O '*/PKG-INFO' | view -\n\n    poetry publish --dry-run\n    poetry publish -u __token__ -p <OWL-RL PyPI Token>\n",
    'author': 'Nicholas Car',
    'author_email': 'nick@kurrawong.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
