# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPint(PythonPackage):
    # BEGIN VERSIONS
    version("0.23", sha256="df79b6b5f1beb7ed0cd55d91a0766fc55f972f757a9364e844958c05e8eb66f9", url="https://pypi.org/packages/76/1a/096c91c2006648fe28564e5884d59978962afe98de74b1c01bb5913d033f/Pint-0.23-py3-none-any.whl")
    version("0.22", sha256="6e2b3c5c2b4d9b516608bc860a417a39d66eb99c958f36540cf931d2c2e9f80f", url="https://pypi.org/packages/ba/70/f3fa88f899cdf17535ddb75c4d4f1d540199524d9dd7479e66aac777de47/Pint-0.22-py3-none-any.whl")
    version("0.21.1", sha256="230ebccc312693117ee925c6492b3631c772ae9f7851a4e86080a15e7be692d8", url="https://pypi.org/packages/49/bc/7ef2a654754cc3179af8df837485931f0874d96e111005a6246c1ed695f2/Pint-0.21.1-py3-none-any.whl")
    version("0.21", sha256="998b695e84a34d11702da4a8b9457a39bb5c7ab5ec68db90e948e30878e421f1", url="https://pypi.org/packages/54/28/2284576fcd92a5bb645df72e86934137238a0a1dbdaae06141767446e3a1/Pint-0.21-py3-none-any.whl")
    version("0.20.1", sha256="68afe65665542ee3ec99f69f043b1d39bfe7c6d61b786940157138fd08b838fb", url="https://pypi.org/packages/db/1b/97d8fd443d89e8d39b3aaa95aa70a184f752b68d2cc803f7fedab8dfd81f/Pint-0.20.1-py3-none-any.whl")
    version("0.20", sha256="721dd1f19e5ed896971a25f3f971ae65b28b1200853cc22ac8f471f8b801b907", url="https://pypi.org/packages/82/4c/aa582175b0eacdc83975f703a517122f62be681e85aefc304bad25f37f44/Pint-0.20-py3-none-any.whl")
    version("0.19.2", sha256="e1d4989ff510b378dad64f91711e7bdabe5ca78d75b06a18569ac454678c4baf", url="https://pypi.org/packages/eb/59/73fd3810d94f2c87aacc79f4e578e1d81df6f0f2800b80b7d3c4fb4e3a2d/Pint-0.19.2.tar.gz")
    version("0.19.1", sha256="3e5913e4ad125f672f72e19e06a8cb1f6d36a4922b6e5a49e04ff882511f82c8", url="https://pypi.org/packages/53/6e/bf5716b7f2355fcae48b2b862c29898ea8948729056a1a9a233b01eaa1d1/Pint-0.19.1.tar.gz")
    version("0.19", sha256="7c3afe8488aeda03bbeb3ffc74f3b3ba7b16903161356eb0cfecf5828f3aed2f", url="https://pypi.org/packages/04/b6/6dbd11e8c7da1a1b8881a733a357df1b6608a87d970047ffd060c64f200b/Pint-0.19.tar.gz")
    version("0.18", sha256="4b37f3c470639ea6f96b0026c3364bde30631fa737092bdaf18ad3f4f76f252f", url="https://pypi.org/packages/0a/98/98b3c6d954b6bd8531c611fb24be53ccc66438f493b05ec4b107942e27b7/Pint-0.18-py2.py3-none-any.whl")
    version("0.17", sha256="6593c5dfaf2f701c54f17453191dff05e90ec9ebc3d1901468a59cfcb3289a4c", url="https://pypi.org/packages/33/de/53a77b82553579affab7438d299f850acbc1c4dd741c5ce52594513cb0ef/Pint-0.17-py2.py3-none-any.whl")
    version("0.11", sha256="5690c85948dfb283382aa73357c3d5a333e8c7d818be7d8643db18e07597dd99", url="https://pypi.org/packages/9d/db/7a2204b03c22069839958df5723eb2718d50c33052e0da84c9a83de14ea4/Pint-0.11-py2.py3-none-any.whl")
    version("0.10.1", sha256="d5b5bcb570b2a8e0a598621fc41684497ff248f418bbfe00f69bd6e13caa14b8", url="https://pypi.org/packages/90/f9/2bdadf95328c02e57a79e5370d1e911a9c6fdb9952b6c4de44d6c7052978/Pint-0.10.1-py2.py3-none-any.whl")
    version("0.10", sha256="b13b3e7c2fcbcb7662010cc4550d7e5372735ace0b7abf00dc26d0a400f56545", url="https://pypi.org/packages/59/2d/f6454ed8f89ab7b8ebb56c5e11ff0a8c519899fb2182751d42b157148580/Pint-0.10-py2.py3-none-any.whl")
    version("0.9", sha256="7ece3f639ad58073ce49982b022d464014e6d91d0b3eaa89c8e8ea9c38e32659", url="https://pypi.org/packages/15/9d/bf177ebbc57d25e9e296addc14a1303d1e34d7964af5df428a8332349c42/Pint-0.9-py2.py3-none-any.whl")
    version("0.8.1", sha256="afcf31443a478c32bbac4b00337ee9026a13d0e2ac83d30c79151462513bb0d4", url="https://pypi.org/packages/1e/40/6938f7d544eef208a8183c2c80624289e8a4f4e0aea43f4658b9527077de/Pint-0.8.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.22-rc1:")
        depends_on("py-packaging", when="@0.13:0.18")
        depends_on("py-setuptools", when="@0.10:0.15")
        depends_on("py-typing-extensions", when="@0.22-rc1:")
    # END DEPENDENCIES

