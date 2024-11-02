# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['optimism']

package_data = \
{'': ['*'], 'optimism': ['assets/*']}

install_requires = \
['python-dotenv==1.0.0', 'web3==6.11.1']

setup_kwargs = {
    'name': 'optimism-python',
    'version': '0.3.1',
    'description': 'Unofficial Python Client for the OP-Stack',
    'long_description': '# Optimism-Python: Unofficial Python Client for the OP-Stack\n\n> [!WARNING]\n> Reference SDK is still under active development so the repository might be temporarily out of date.\n\n<div align="center">\n    <img src="https://github.com/rafalum/optimism-python/assets/38735195/12cb4de6-7cb5-403d-993b-5461febd5b72" width=200 height=200 />\n</div>\n\n\nThis library is a Python implementation of the [OP-Stack SDK](https://sdk.optimism.io/). It tries to mirror some of the core functionalities such as:\n\n- providing easy access to the OP-Stack contracts\n- bridging of assets from L1 to L2 (deposits) and vice-versa (withdrawls)\n- creating withdrawl proofs\n\n## Getting started\n\n### Installation\n\n```bash\npip install optimism-python\n```\n\n### Deposit ETH to L2\n\n```python\nfrom web3 import Web3\nfrom optimism import CrossChainMessenger\nfrom optimism.types import Chains\n\n# Create a node provider for each chain\nprovider_l1 = Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/<your-alchemy-key>"))\nprovider_l2 = Web3(Web3.HTTPProvider("https://optimism-mainnet.g.alchemy.com/v2/<your-alchemy-key>"))\n\n# Specify an account for each chain (can be the same)\naccount_l1 = provider_l1.eth.account.from_key("<your-private-key>")\naccount_l2 = provider_l2.eth.account.from_key("<your-private-key>")\n\n# Create a messenger instance\nmessenger = CrossChainMessenger(chain_l1=Chains.ETHEREUM_MAINNET,\n                                chain_l2=Chains.OPTIMISM_MAINNET,\n                                account_l1=account_l1, \n                                account_l2=account_l2,\n                                provider_l1=provider_l1,\n                                provider_l2=provider_l2)\n\n# Deposit 1 ETH to L2\nmessenger.deposit_eth(10**18)\n```\n',
    'author': 'rafalum',
    'author_email': 'rafalum@pm.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rafalum/optimism-python',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
