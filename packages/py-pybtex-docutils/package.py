# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPybtexDocutils(PythonPackage):
    # BEGIN VERSIONS
    version("1.0.3", sha256="8fd290d2ae48e32fcb54d86b0efb8d573198653c7e2447d5bec5847095f430b9", url="https://pypi.org/packages/11/b1/ce1f4596211efb5410e178a803f08e59b20bedb66837dcf41e21c54f9ec1/pybtex_docutils-1.0.3-py3-none-any.whl")
    version("1.0.2", sha256="6f9e3c25a37bcaac8c4f69513272706ec6253bb708a93d8b4b173f43915ba239", url="https://pypi.org/packages/ef/9b/d14374c7ef41e8fcf214a7d563407d7f7215d82d3dab53b0329535d251b5/pybtex_docutils-1.0.2-py3-none-any.whl")
    version("1.0.1", sha256="42e379bd1d5473b9fd7be4b3a64ca291d4fdc9ae6c6854e52d1d0157c955bbfa", url="https://pypi.org/packages/f5/ea/369444b3bb77295350c268bc6c0dc0cf4dece20c4c61487012abf4a8e96a/pybtex_docutils-1.0.1-py3-none-any.whl")
    version("1.0.0", sha256="8a2ca2d89b70be3a722d73aeb64d57065c79000f54719672dd9a9a86288d13f7", url="https://pypi.org/packages/6a/4b/060b0c0e3b18ae927fa6400233661b3af064571dba4fac92372030ed640b/pybtex_docutils-1.0.0-py3-none-any.whl")
    version("0.2.2", sha256="4beb8c36f4f4a5a3f437cc2ff7dea8c1c7fe655d79c1229cb432af141884875b", url="https://pypi.org/packages/e9/97/066aa09efc1a1f969ffc6ca0e697787a3b8eb9e847a9b5973c0f73119318/pybtex_docutils-0.2.2-py2.py3-none-any.whl")
    version("0.2.1", sha256="920ae9850750dd61abe00d9fd88f4a5f9099e40af0b84b2119b8b44a479115d2", url="https://pypi.org/packages/5f/7f/f2107bd9b1cc38a83cd18e9ab8608d8905e35fbd6e936e32354531e3ae75/pybtex_docutils-0.2.1-py2.py3-none-any.whl")
    version("0.2.0", sha256="9e7697788b0cd34f5ae66b686fa0836a33b4367e75d0fbe16500b1e1f2485c7a", url="https://pypi.org/packages/92/00/1ff590bc33ddef439c8fee074578aca58f08129ec2fc2c8114351d2c55e3/pybtex-docutils-0.2.0.zip")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-docutils@0.14:", when="@1.0.3:")
        depends_on("py-docutils@0.8:", when="@0.2.1:1.0.2")
        depends_on("py-pybtex@0.16:", when="@0.2.1:")
        depends_on("py-six", when="@0.2.1:0")
    # END DEPENDENCIES

