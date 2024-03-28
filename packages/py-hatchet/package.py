# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHatchet(PythonPackage):
    # BEGIN VERSIONS
    version("1.3.0", sha256="d78571be64e37a8d0714e1cd45c9f9b1181650e0d4b8df288b3ed4781667f461", url="https://pypi.org/packages/df/76/2b4f00d711f326c7302f49c7dab02e050ee220368cf9baa9ef8c0d143607/hatchet-1.3.0.tar.gz")
    version("1.2.0", sha256="d37e83bc208ad035be1508ce15ab60516140493526f2dd82e68de03bc476ec46", url="https://pypi.org/packages/63/ac/01f8b3e87945c9e2638952d0e69f80fa45126f1b02604ca0afce52db6f98/hatchet-1.2.0-py2.py3-none-any.whl")
    version("1.1.0", sha256="d516cb7b235dd2ab3c1e59a039b27784e190520d9726a5db5ae1aa438d4fdbd5", url="https://pypi.org/packages/17/f9/237b0c0eada25023c461e88d7bb22511811e8107662b10aa46872eb6d92e/hatchet-1.1.0.tar.gz")
    version("1.0.1", sha256="f20e14c1e1ad7c3a98d6b2fcfd944393cabd4fc6ea3d419459d5d79dd5d6660a", url="https://pypi.org/packages/46/7d/fa56889c35b04cfb27624ec6c2baa5afa0cc30893f1e5d55310dae187a89/hatchet-1.0.1.tar.gz")
    version("1.0.0", sha256="89c95f21de350cc23c2042c36cfb62dc7cc4265e5dc934052485526241f92361", url="https://pypi.org/packages/52/29/96a4cff689cdaeedc9c98422b727f6cc51061a0846a8418aa3bcd83a8d57/hatchet-1.0.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-matplotlib", when="@1.2")
        depends_on("py-numpy", when="@1.2")
        depends_on("py-pandas", when="@1.2")
        depends_on("py-pydot", when="@1.2")
        depends_on("py-pyyaml", when="@1.2")
    # END DEPENDENCIES

