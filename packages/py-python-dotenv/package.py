# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonDotenv(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.0.1", sha256="f7b63ef50f1b690dddf550d03497b66d609393b40b564ed0d674909a68ebf16a", url="https://pypi.org/packages/6a/3e/b68c118422ec867fa7ab88444e1274aa40681c606d59ac27de5a5588f082/python_dotenv-1.0.1-py3-none-any.whl")
    version("1.0.0", sha256="f5971a9226b701070a4bf2c38c89e5a3f0d64de8debda981d1db98583009122a", url="https://pypi.org/packages/44/2f/62ea1c8b593f4e093cc1a7768f0d46112107e790c3e478532329e434f00b/python_dotenv-1.0.0-py3-none-any.whl")
    version("0.21.1", sha256="41e12e0318bebc859fcc4d97d4db8d20ad21721a6aa5047dd59f090391cb549a", url="https://pypi.org/packages/64/62/f19d1e9023aacb47241de3ab5a5d5fedf32c78a71a9e365bb2153378c141/python_dotenv-0.21.1-py3-none-any.whl")
    version("0.21.0", sha256="1684eb44636dd462b66c3ee016599815514527ad99965de77f43e0944634a7e5", url="https://pypi.org/packages/2d/10/ff4f2f5b2a420fd09e1331d63cc87cf4367c5745c0a4ce99cea92b1cbacb/python_dotenv-0.21.0-py3-none-any.whl")
    version("0.20.0", sha256="d92a187be61fe482e4fd675b6d52200e7be63a12b724abbf931a40ce4fa92938", url="https://pypi.org/packages/30/5f/2e5c564bd86349fe6b82ca840f46acf6f4bb76d79ba9057fce3d3e008864/python_dotenv-0.20.0-py3-none-any.whl")
    version("0.19.2", sha256="32b2bdc1873fd3a3c346da1c6db83d0053c3c62f28f1f38516070c4c8971b1d3", url="https://pypi.org/packages/0e/f1/0317f4b2c5284075a2154fe95539b43c0acecbcb86fe80fcb2645803edd9/python_dotenv-0.19.2-py2.py3-none-any.whl")
    version("0.19.1", sha256="bbd3da593fc49c249397cbfbcc449cf36cb02e75afc8157fcc6a81df6fb7750a", url="https://pypi.org/packages/af/85/7433188f5811856dabe0c7bccc832a23c2fd49b48fc57373d9c10747a1ea/python_dotenv-0.19.1-py2.py3-none-any.whl")
    version("0.19.0", sha256="aae25dc1ebe97c420f50b81fb0e5c949659af713f31fdb63c749ca68748f34b1", url="https://pypi.org/packages/f5/d6/4b6268fad900fcb064e4344aa563b22688f0b38dcd857b500b2b5cc445c6/python_dotenv-0.19.0-py2.py3-none-any.whl")
    version("0.18.0", sha256="dd8fe852847f4fbfadabf6183ddd4c824a9651f02d51714fa075c95561959c7d", url="https://pypi.org/packages/5c/0c/9c5d5dd254e9e7a32d34777cc6fd33cbeb174744061458b88470aecbd1d6/python_dotenv-0.18.0-py2.py3-none-any.whl")
    version("0.17.1", sha256="00aa34e92d992e9f8383730816359647f358f4a3be1ba45e5a5cefd27ee91544", url="https://pypi.org/packages/26/1f/ae3d06ec877df31f49448d24eee7198549edae2af00da60c85dad93e343f/python_dotenv-0.17.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("cli", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-click@5:", when="@0.10.3:0.10.4,0.11:+cli")
    # END DEPENDENCIES

