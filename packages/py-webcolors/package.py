# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyWebcolors(PythonPackage):
    # BEGIN VERSIONS
    version("1.13", sha256="29bc7e8752c0a1bd4a1f03c14d6e6a72e93d82193738fa860cbff59d0fcc11bf", url="https://pypi.org/packages/d5/e1/3e9013159b4cbb71df9bd7611cbf90dc2c621c8aeeb677fc41dad72f2261/webcolors-1.13-py3-none-any.whl")
    version("1.12", sha256="d98743d81d498a2d3eaf165196e65481f0d2ea85281463d856b1e51b09f62dce", url="https://pypi.org/packages/af/a9/71beaebcacd7dd848af470740dbe7f39aa6bd23a60b8162f8c050090eed4/webcolors-1.12-py3-none-any.whl")
    version("1.11.1", sha256="b8cd5d865a25c51ff1218f0c90d0c0781fc64312a49b746b320cf50de1648f6e", url="https://pypi.org/packages/12/05/3350559de9714b202e443a9e6312937341bd5f79f4e4f625744295e7dd17/webcolors-1.11.1-py3-none-any.whl")
    version("1.11", sha256="d51dee95a097812919eb445167a9c1887942cc3ecdfda4c5e50241d2376ed58b", url="https://pypi.org/packages/1f/7e/dc100f3c92c3c910d3961163a8dec833c635e0fd54fd9ddb3560e27da86b/webcolors-1.11-py3-none-any.whl")
    version("1.10", sha256="2559b4f4694bfcd61c87ee06acad921bd2fdbf0c844bee65fc844c6910c413dd", url="https://pypi.org/packages/8b/ff/c21df7e08e68a1a84b947992c07dfed9cfe7219d068cb7728358d065c877/webcolors-1.10-py2.py3-none-any.whl")
    version("1.9.1", sha256="771adfb75a8d9189724de748b2e9564edf64104726bff0c4f6e11d15635e6517", url="https://pypi.org/packages/b0/d8/cfb0da8bcbe9fd0cbeaf24d320f0353724de4f14b720338d9fd38df6c92d/webcolors-1.9.1-py2.py3-none-any.whl")
    version("1.9", sha256="49f887d15e86cee92f3c5a716de23012fe769540fc02e3d2dbc57dc707a0dbfd", url="https://pypi.org/packages/79/89/d39bfded8cea46b3339200f793af3e1c41b6011332af7048eef93b988ef1/webcolors-1.9-py2.py3-none-any.whl")
    version("1.8.1", sha256="b3b88e5ef2b35fa9e01e3fabe99dddf49da074459c44774c59f3ccab3be4f121", url="https://pypi.org/packages/1d/44/c4902683be73beba20afd299705e11f0a753a01cc7f9d6a070841848605b/webcolors-1.8.1-py2.py3-none-any.whl")
    version("1.8", sha256="da3cb551060f46f417341b041b36d329d699c125a13a4412dde5c2e310d63344", url="https://pypi.org/packages/8d/79/91fdb622b9fdacd7acde3e65048857999981006720f0f4a1b8dfe66a7c46/webcolors-1.8.tar.gz")
    version("1.7", sha256="e47e68644d41c0b1f1e4d939cfe4039bdf1ab31234df63c7a4f59d4766487206", url="https://pypi.org/packages/1c/11/d9fb5a7c872a941ad8b30a4be191253d5a9028834c4d69eab55bb6bc60be/webcolors-1.7.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-six", when="@1.9:1.10")
    # END DEPENDENCIES

