##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAgateExcel(PythonPackage):
    version("0.4.1", sha256="398f214cb24e3debcb6cc75f52dc558dee84d594f5f4b5e73997299c6c786158", url="https://pypi.org/packages/d6/6f/5d71389b715654dc636180af8b33923926f73c4cf89450813c9380cbb3cf/agate_excel-0.4.1-py2.py3-none-any.whl")
    version("0.4.0", sha256="f020e7ec99958f88587302096dcf4f680611e3fd9f3ff12c7add58943587f9fb", url="https://pypi.org/packages/87/8d/9d54b55b1af3de4cc0588bedbbe8d0ef0219f6715ea994661ee1bbfaf6bd/agate_excel-0.4.0-py2.py3-none-any.whl")
    version("0.3.0", sha256="c45e0701528fb605bd1b329e1f7a0cfd9342b3a82321c96dbc02098a320870c1", url="https://pypi.org/packages/fc/df/c83c8e8020c4f33ba6ee772d8cb2fb10aa580159e3ce0d3ff6086d043209/agate_excel-0.3.0-py2.py3-none-any.whl")
    version("0.2.5", sha256="8963da01e0a09438a9d2743573948c14689f43e7e01bdd9add9865e9e24e294b", url="https://pypi.org/packages/f0/2b/798066f26f4d07ead84b840b7c88a602ce7d53d99f19583c98d374e162f7/agate_excel-0.2.5-py2.py3-none-any.whl")
    version("0.2.4", sha256="30e897bef3424d9e0782c06f96e1a61f230c53ef2487cae0528f70cfb64f4e4e", url="https://pypi.org/packages/a8/1e/3b67010b3adbfecb99dfbc7c4c46b26cf9922a4b6e0a1706bf859c28dcf0/agate_excel-0.2.4-py2.py3-none-any.whl")
    version("0.2.3", sha256="8f255ef2c87c436b7132049e1dd86c8e08bf82d8c773aea86f3069b461a17d52", url="https://pypi.org/packages/a9/cd/ba7ce638900a91f00e6ebaa72c46fc90bfc13cb595071cee82c96057d5d6/agate-excel-0.2.3.tar.gz")
    version("0.2.2", sha256="8923f71ee2b5b7b21e52fb314a769b28fb902f647534f5cbbb41991d8710f4c7", url="https://pypi.org/packages/02/c0/b82c6f830946203ec16d83eb8a6b250309ba8dcec14640b94eb69d88d30c/agate-excel-0.2.2.tar.gz")

    with default_args(type="run"):
        depends_on("py-agate@1.5:", when="@0.2.4:")
        depends_on("py-olefile", when="@0.2.4:")
        depends_on("py-openpyxl@2.3:", when="@0.2.4:")
        depends_on("py-six", when="@0.2.5:0.2")
        depends_on("py-xlrd@0.9.4:", when="@0.2.4:")

