# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['exasol_advanced_analytics_framework',
 'exasol_advanced_analytics_framework.deployment',
 'exasol_advanced_analytics_framework.query_handler',
 'exasol_advanced_analytics_framework.query_handler.context',
 'exasol_advanced_analytics_framework.query_handler.context.proxy',
 'exasol_advanced_analytics_framework.query_handler.query',
 'exasol_advanced_analytics_framework.query_result',
 'exasol_advanced_analytics_framework.udf_communication',
 'exasol_advanced_analytics_framework.udf_communication.discovery',
 'exasol_advanced_analytics_framework.udf_communication.discovery.localhost',
 'exasol_advanced_analytics_framework.udf_communication.discovery.multi_node',
 'exasol_advanced_analytics_framework.udf_communication.peer_communicator',
 'exasol_advanced_analytics_framework.udf_communication.peer_communicator.background_thread',
 'exasol_advanced_analytics_framework.udf_communication.peer_communicator.background_thread.connection_closer',
 'exasol_advanced_analytics_framework.udf_communication.socket_factory',
 'exasol_advanced_analytics_framework.udf_framework',
 'exasol_advanced_analytics_framework.udf_utils.testing',
 'exasol_data_science_utils_python',
 'exasol_data_science_utils_python.schema',
 'exasol_data_science_utils_python.udf_utils',
 'exasol_data_science_utils_python.udf_utils.testing',
 'exasol_data_science_utils_python.utils']

package_data = \
{'': ['*'],
 'exasol_advanced_analytics_framework': ['lua/src/*',
                                         'lua/test/*',
                                         'resources/outputs/*',
                                         'resources/templates/*']}

install_requires = \
['click>=8.0.4,<9.0.0',
 'exasol-bucketfs>=0.6.0,<1.0.0',
 'importlib-resources>=6.4.0,<7.0.0',
 'jinja2>=3.0.3,<4.0.0',
 'nox>=2024.4.15,<2025.0.0',
 'pandas>=1.1.0,<2.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'pyexasol>=0.25.0,<1.0.0',
 'pyzmq>=26.0.3,<27.0.0',
 'sortedcontainers>=2.4.0,<3.0.0',
 'structlog>=24.2.0,<25.0.0',
 'typeguard>=4.0.0,<5.0.0']

setup_kwargs = {
    'name': 'exasol-advanced-analytics-framework',
    'version': '0.1.0',
    'description': 'Framework for building complex data analysis algorithms with Exasol',
    'long_description': '# Exasol Advanced Analytics Framework\n\n**This project is at an early development stage.**\n\nFramework for building complex data analysis algorithms with Exasol.\n\n\n## Information for Users\n\n- [User Guide](doc/user_guide/user_guide.md)\n- [System Requirements](doc/system_requirements.md)\n- [Design](doc/design.md)\n- [License](LICENSE)\n\n## Information for Developers\n\n- [Developers Guide](doc/developer_guide/developer_guide.md)\n\n',
    'author': 'Umit Buyuksahin',
    'author_email': 'umit.buyuksahin@exasol.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/exasol/advanced-analytics-framework',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4',
}


setup(**setup_kwargs)
