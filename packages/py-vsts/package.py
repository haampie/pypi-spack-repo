# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyVsts(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.1.25", sha256="c5595a42c9447888ebc91494d2db03c2b867cbca9f1f5f05c113261b92383e35", url="https://pypi.org/packages/9a/4a/c9a5c90659bf0df577067cf8baf9c690501306290e5688d8aeae07fbd9f8/vsts-0.1.25-py3-none-any.whl")
    version("0.1.24", sha256="b504249260895e524eb3440011a2018194365cb063c73df787e4c36b468ab9ab", url="https://pypi.org/packages/a3/26/06f63ba7d2711f92ca902e48e0e8aa0a9af1e177516e83d4a3276e220f7e/vsts-0.1.24-py3-none-any.whl")
    version("0.1.23", sha256="3c419bb5e3231671adf5506574bdfeb2f8cb85775eb28ad9c1c7923180f63cb6", url="https://pypi.org/packages/67/8f/81cc18b746b3bb4a0a11b4953bb63b314a25a5dd62f9ad8d3e941454e60d/vsts-0.1.23-py3-none-any.whl")
    version("0.1.22", sha256="8aff1e9ebca6eae5a55841af0d91bdf5c6e4f0b779fc06d8bfb7cba5ac46936f", url="https://pypi.org/packages/f9/33/c0beaf75899260c2f4715cccba9cd7ce6000f9f7676b885479163357f7e4/vsts-0.1.22-py3-none-any.whl")
    version("0.1.21", sha256="76c9dec28ab9baf75a66f2f2c15bf08c5eac7887701bccd306d7cc63c5335801", url="https://pypi.org/packages/75/52/9b5e33a2c11179fa707785dd035fde7c5a9b8d1c72c321e8f049575c8b4c/vsts-0.1.21-py3-none-any.whl")
    version("0.1.20", sha256="a3d274896914a547eee3b7549bae6fc54647ff8473b75980f930f87f83713301", url="https://pypi.org/packages/0b/9e/69ddfa7aa9305e7bb182db0eea9cc38536b8475bc62d6c6736d09ce72e28/vsts-0.1.20-py3-none-any.whl")
    version("0.1.19", sha256="b12ffa326846f75cf432d41c26a9377d1d6af0c29d77a488700611c5c0f5df6e", url="https://pypi.org/packages/3e/1c/88a578c6e1b21a1675a68c6fbeb40285b56499bedef150d317aa82f4b143/vsts-0.1.19-py3-none-any.whl")
    version("0.1.18", sha256="3729113d5314a7058cedbbe888bca5f928e90b61a9e003571b5b0752117dfd68", url="https://pypi.org/packages/9e/15/9df17f05a1e4639da672652de8bc4ba1da5a0284aa4c6275c11116540d67/vsts-0.1.18-py3-none-any.whl")
    version("0.1.17", sha256="0ca15d1fbfdc03b4f46b778f0ac5d19858c6ae726ec4806080f451dd5e186334", url="https://pypi.org/packages/ed/f3/08215ff6350fdabece7228c6bfee0db33b7a9450f8b5cb75f1a35b6bc4c0/vsts-0.1.17-py3-none-any.whl")
    version("0.1.16", sha256="35d109a09b6c48ef76f6f97d730c6f9d04d566ccc17f8e9ce0dbcaa371fff742", url="https://pypi.org/packages/95/5e/34d3ff1ae23c87872522f31871227a26570b06a956f7ddf1791ec4a70f9e/vsts-0.1.16-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-msrest@0.6.0:0.6", when="@0.1.20:")
        depends_on("py-msrest@0.5", when="@0.1.18:0.1.19")
        depends_on("py-msrest@0.5:", when="@0.1.13:0.1.17")
    # END DEPENDENCIES

