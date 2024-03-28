# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyasn1Modules(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.4.0", sha256="be04f15b66c206eed667e0bb5ab27e2b1855ea54a842e5037738099e8ca4ae0b", url="https://pypi.org/packages/13/68/8906226b15ef38e71dc926c321d2fe99de8048e9098b5dfd38343011c886/pyasn1_modules-0.4.0-py3-none-any.whl")
    version("0.3.0", sha256="d3ccd6ed470d9ffbc716be08bd90efbd44d0734bc9303818f7336070984a162d", url="https://pypi.org/packages/cd/8e/bea464350e1b8c6ed0da3a312659cb648804a08af6cacc6435867f74f8bd/pyasn1_modules-0.3.0-py2.py3-none-any.whl")
    version("0.2.8", sha256="a50b808ffeb97cb3601dd25981f6b016cbb3d31fbf57a8b8a87428e6158d0c74", url="https://pypi.org/packages/95/de/214830a981892a3e286c3794f41ae67a4495df1108c3da8a9f62159b9a9d/pyasn1_modules-0.2.8-py2.py3-none-any.whl")
    version("0.2.7", sha256="b6ada4f840fe51abf5a6bd545b45bf537bea62221fa0dde2e8a553ed9f06a4e3", url="https://pypi.org/packages/52/50/bb4cefca37da63a0c52218ba2cb1b1c36110d84dcbae8aa48cd67c5e95c2/pyasn1_modules-0.2.7-py2.py3-none-any.whl")
    version("0.2.6", sha256="e30199a9d221f1b26c885ff3d87fd08694dbbe18ed0e8e405a2a7126d30ce4c0", url="https://pypi.org/packages/be/70/e5ea8afd6d08a4b99ebfc77bd1845248d56cfcf43d11f9dc324b9580a35c/pyasn1_modules-0.2.6-py2.py3-none-any.whl")
    version("0.2.5", sha256="f309b6c94724aeaf7ca583feb1cc70430e10d7551de5e36edfc1ae6909bcfb3c", url="https://pypi.org/packages/91/f0/b03e00ce9fddf4827c42df1c3ce10c74eadebfb706231e8d6d1c356a4062/pyasn1_modules-0.2.5-py2.py3-none-any.whl")
    version("0.2.4", sha256="79580acf813e3b7d6e69783884e6e83ac94bf4617b36a135b85c599d8a818a7b", url="https://pypi.org/packages/da/98/8ddd9fa4d84065926832bcf2255a2b69f1d03330aa4d1c49cc7317ac888e/pyasn1_modules-0.2.4-py2.py3-none-any.whl")
    version("0.2.3", sha256="642afdabb681d39f5948fd5477764d94faf17ce40e5691e9998b52815fbb4e71", url="https://pypi.org/packages/59/84/339c2de112d7448d7d4c500b8016783d9eac8981f89ec1d58fdd4685d97f/pyasn1_modules-0.2.3-py2.py3-none-any.whl")
    version("0.2.2", sha256="a38a8811ea784c0136abfdba73963876328f66172db21a05a82f9515909bfb4e", url="https://pypi.org/packages/19/02/fa63f7ba30a0d7b925ca29d034510fc1ffde53264b71b4155022ddf3ab5d/pyasn1_modules-0.2.2-py2.py3-none-any.whl")
    version("0.2.1", sha256="47fb6757ab78fe966e7c58b2030b546854f78416d653163f0ce9290cf2278e8b", url="https://pypi.org/packages/e9/51/bcd96bf6231d4b2cc5e023c511bee86637ba375c44a6f9d1b4b7ad1ce4b9/pyasn1_modules-0.2.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyasn1@0.4.6:", when="@0.4:")
        depends_on("py-pyasn1@0.4.6:0.5", when="@0.3")
        depends_on("py-pyasn1@0.4.6:0.4", when="@0.2.6:0.2")
        depends_on("py-pyasn1@0.4", when="@0.2:0.2.5")
    # END DEPENDENCIES

