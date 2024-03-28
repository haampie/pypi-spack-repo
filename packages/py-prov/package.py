# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyProv(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.0.0", sha256="aaccc7c6ad6ec662fd1561c872991f13cd7df368d6dcab9cbac19fccc491d970", url="https://pypi.org/packages/cf/8d/9a5110845c6b117d203e3ca9eec5ee79bed29cef508c8415fbc85e900150/prov-2.0.0-py3-none-any.whl")
    version("1.5.1", sha256="5c930cbbd05424aa3066d336dc31d314dd9fa0280caeab064288e592ed716bea", url="https://pypi.org/packages/8e/fb/2c4c618185be2bda327f9dacd16b3122cc938809f19df7be840595d0e584/prov-1.5.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("dot", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-lxml@3.3.5:", when="@1.5.2:")
        depends_on("py-lxml", when="@1.5.1")
        depends_on("py-networkx@2:", when="@1.5.2:")
        depends_on("py-networkx", when="@1.5.1")
        depends_on("py-pydot@1.2:", when="@1.5.1:+dot")
        depends_on("py-python-dateutil@2.2:", when="@1.5.2:")
        depends_on("py-python-dateutil", when="@1.5.1")
        depends_on("py-rdflib@4.2.1:", when="@1.5.1:")
        depends_on("py-six@1.9:", when="@1.5.1:1")
    # END DEPENDENCIES

