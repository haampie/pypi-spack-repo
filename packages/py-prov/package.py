##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyProv(PythonPackage):
    version("2.0.0", sha256="aaccc7c6ad6ec662fd1561c872991f13cd7df368d6dcab9cbac19fccc491d970", url="https://pypi.org/packages/cf/8d/9a5110845c6b117d203e3ca9eec5ee79bed29cef508c8415fbc85e900150/prov-2.0.0-py3-none-any.whl")
    version("1.5.3", sha256="b9c553cc0775bf193eb62de69e2a2b3bab545ab8e6bf597be243e8f0916e1d1b", url="https://pypi.org/packages/aa/f1/85f277cf15ce2fed6f189b220ff14d7b33b21cc7beb95ae48f1255672e74/prov-1.5.3-py2.py3-none-any.whl")
    version("1.5.2", sha256="33a5ad2aabb9fc55fc23446fc11509fee7562d6b3412e63e28d757f4de06a8bc", url="https://pypi.org/packages/5c/1e/ac3989756b8a0262de881f7378783e53b693409273ac5725eab59c028f55/prov-1.5.2-py2.py3-none-any.whl")
    version("1.5.1", sha256="5c930cbbd05424aa3066d336dc31d314dd9fa0280caeab064288e592ed716bea", url="https://pypi.org/packages/8e/fb/2c4c618185be2bda327f9dacd16b3122cc938809f19df7be840595d0e584/prov-1.5.1-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-lxml@3.3.5:", when="@1.5.2:")
        depends_on("py-lxml", when="@1.5.1")
        depends_on("py-networkx@2:", when="@1.5.2:")
        depends_on("py-networkx", when="@1.5.1")
        depends_on("py-python-dateutil@2.2:", when="@1.5.2:")
        depends_on("py-python-dateutil", when="@1.5.1")
        depends_on("py-rdflib@4.2.1:", when="@1.5.1:")
        depends_on("py-six@1.9:", when="@1.5.1:1")

