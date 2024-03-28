# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyVirtualenvwrapper(PythonPackage):
    # BEGIN VERSIONS
    version("4.8.4", sha256="51a1a934e7ed0ff221bdd91bf9d3b604d875afbb3aa2367133503fee168f5bfa", url="https://pypi.org/packages/c1/6b/2f05d73b2d2f2410b48b90d3783a0034c26afa534a4a95ad5f1178d61191/virtualenvwrapper-4.8.4.tar.gz")
    version("4.8.2", sha256="137f7d4509283d798d64509a1a80c57d2d58d900d7a0f827ab67d3104abe232c", url="https://pypi.org/packages/2b/8c/3192e10913ad945c0f0fcb17e9b2679434a28ad58ee31ce0104cba3b1154/virtualenvwrapper-4.8.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-stevedore", when="@:0,4.8:4.8.2,6:")
        depends_on("py-virtualenv", when="@:0,4.8:4.8.2,6:")
        depends_on("py-virtualenv-clone", when="@:0,4.8:4.8.2,6:")
    # END DEPENDENCIES

