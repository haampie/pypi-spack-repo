##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyClickPlugins(PythonPackage):
    version("1.1.1", sha256="5d262006d3222f5057fd81e1623d4443e41dcda5dc815c06b442aa3c02889fc8", url="https://pypi.org/packages/e9/da/824b92d9942f4e472702488857914bdd50f73021efea15b4cad9aca8ecef/click_plugins-1.1.1-py2.py3-none-any.whl")
    version("1.1", sha256="c313f8af17036d2667d0165bf9030f672a6d5f4b9c084090ada5584b9bd7de13", url="https://pypi.org/packages/2e/28/32c4a7c032288dfdb646722ffaaaa79c1e27485da5aa3e189054f852bff3/click_plugins-1.1-py2.py3-none-any.whl")
    version("1.0.4", sha256="b1ee1ccc9421c73007fe290680d97984eb6eaf5f4512b7620c6aa46031d6cb6b", url="https://pypi.org/packages/95/dd/fef84cf1678418f241ef542c0288bdf215bdd3e35f1fe03dc5223a2e80ba/click_plugins-1.0.4-py2.py3-none-any.whl")
    version("1.0.3", sha256="7acc5e7eedd2dfd719714e8d53ae99030b5357aed661d0b06dacd6c2d583d7c5", url="https://pypi.org/packages/77/05/da5c9e19457f20cadfe22c397cd3852577066066f63e40f2baa0831b1693/click-plugins-1.0.3.tar.gz")
    version("1.0.2", sha256="e30d234a5d20ce36f4cad4288a72d00d4b1d0fa99684dfb2b81fc061ce70c89a", url="https://pypi.org/packages/cb/cc/22f0fb5fa1cb8399b174b83579df3f4e03bf716b565e3a6eddde1e5a4ae4/click_plugins-1.0.2-py2.py3-none-any.whl")
    version("1.0.1", sha256="94e6e289e9f10dfe85a35f54891bd071b1640d5b08777995457f38c282e59f67", url="https://pypi.org/packages/ba/ef/0aceb19f37878751c650979bbcd3fa45cbbb8ce15d3e98252c710a2e2276/click-plugins-1.0.1.tar.gz")
    version("1.0", sha256="a6260de2625d70ee284b599a8f3096f30adb9b824b647c1234a901a920ae02bc", url="https://pypi.org/packages/41/a3/713ebb70fceb873ff26420d3b9f3bc3b3ef5bd984e312a389fbc86f5d632/click-plugins-1.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-click@4:", when="@1.1:")
        depends_on("py-click@3:", when="@1.0.2,1.0.4:1.0")

