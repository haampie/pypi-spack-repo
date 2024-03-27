##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFs(PythonPackage):
    version("2.4.14", sha256="b298013377f51125b3d7f0c86920de4e3e2d4a83731bd5caf1f1e5bddabe7798", url="https://pypi.org/packages/94/09/868aad9dd6a6cb8c3b8f62e6b7c2393f246c799be6b9f93ee1e783143c80/fs-2.4.14-py2.py3-none-any.whl")
    version("0.5.5-alpha1", sha256="f99287c3205441a0c8cc46d3b7bf9da27372fa40f1dc98dcb86af4b8f888f92c", url="https://pypi.org/packages/1f/9d/ff1f96fa926c04b6692dbb34c4d0bdc123d29122d5ff52f377d456684cca/fs-0.5.5a1.tar.gz")
    version("0.5.4", sha256="ba2cca8773435a7c86059d57cb4b8ea30fda40f8610941f7822d1ce3ffd36197", url="https://pypi.org/packages/04/36/d9d564bd96ef2bffb3e493bbb03f363cbdc3a0b19676621053999be78ea4/fs-0.5.4.tar.gz")

    with default_args(type="run"):
        depends_on("py-appdirs@1.4.3:", when="@2.0.22:")
        depends_on("py-pytz", when="@2.0.22:2.4.15")
        depends_on("py-setuptools", when="@2.0.22:")
        depends_on("py-six@1.10:", when="@2.0.22:")

