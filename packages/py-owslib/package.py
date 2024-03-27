##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOwslib(PythonPackage):
    version("0.25.0", sha256="78cfd1d369d7f225705180de3776f1a69770505b8af2b79728edced85204186f", url="https://pypi.org/packages/00/be/a0288a3d7bcea2038c9111497d905bc998eaa84fcba4f2a7f904c962ecf0/OWSLib-0.25.0-py2.py3-none-any.whl")
    version("0.17.1", sha256="b2e7fd694d3cffcee79317bad492d60c0aa887aea6916517c051c3247b33b5a5", url="https://pypi.org/packages/07/15/9609cbb31c9f7ce729d444c04319c1e68a1ae3fd377a93c7615392c0b1e0/OWSLib-0.17.1.tar.gz")
    version("0.16.0", sha256="ec95a5e93c145a5d84b0074b9ea27570943486552a669151140debf08a100554", url="https://pypi.org/packages/ac/71/ff2fbfa64fca17069ce30fac324533aa686c5cb64e6b5f522faed558848f/OWSLib-0.16.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyproj@2:", when="@0.19.2:0.25")
        depends_on("py-python-dateutil@1.5:", when="@0.19.1:")
        depends_on("py-pytz", when="@0.19.1:")
        depends_on("py-pyyaml", when="@0.19.2:")
        depends_on("py-requests@1:", when="@0.19.1:")

