##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHatchet(PythonPackage):
    version("1.4.0", sha256="afc25d8f358598616a8e3286b2c4916462d4abb72ee0d060ca3a6d1bbbd03174", url="https://pypi.org/packages/03/87/3d6cde1f95c170bd909c07f69a694151bc70fbdca074e0d6387b52d0e93b/hatchet-1.4.0.tar.gz")
    version("1.3.1", sha256="17b36abd4bc8c6d5fed452267634170159062ca3c2534199b1c8378f2f3f1f28", url="https://pypi.org/packages/be/75/904c27e3d96d73d5743257caaf820564b0ac3be3497ec2765200ed5241f9/hatchet-1.3.1.tar.gz")
    version("1.3.0", sha256="d78571be64e37a8d0714e1cd45c9f9b1181650e0d4b8df288b3ed4781667f461", url="https://pypi.org/packages/df/76/2b4f00d711f326c7302f49c7dab02e050ee220368cf9baa9ef8c0d143607/hatchet-1.3.0.tar.gz")
    version("1.2.0", sha256="d37e83bc208ad035be1508ce15ab60516140493526f2dd82e68de03bc476ec46", url="https://pypi.org/packages/63/ac/01f8b3e87945c9e2638952d0e69f80fa45126f1b02604ca0afce52db6f98/hatchet-1.2.0-py2.py3-none-any.whl")
    version("1.1.0", sha256="d516cb7b235dd2ab3c1e59a039b27784e190520d9726a5db5ae1aa438d4fdbd5", url="https://pypi.org/packages/17/f9/237b0c0eada25023c461e88d7bb22511811e8107662b10aa46872eb6d92e/hatchet-1.1.0.tar.gz")
    version("1.0.1", sha256="f20e14c1e1ad7c3a98d6b2fcfd944393cabd4fc6ea3d419459d5d79dd5d6660a", url="https://pypi.org/packages/46/7d/fa56889c35b04cfb27624ec6c2baa5afa0cc30893f1e5d55310dae187a89/hatchet-1.0.1.tar.gz")
    version("1.0.0", sha256="89c95f21de350cc23c2042c36cfb62dc7cc4265e5dc934052485526241f92361", url="https://pypi.org/packages/52/29/96a4cff689cdaeedc9c98422b727f6cc51061a0846a8418aa3bcd83a8d57/hatchet-1.0.0.tar.gz")
    version("0.0.3", sha256="ee20a1b323b6111e79b3cf6018e1becf87e12ea74eea34f7e02326831759fb80", url="https://pypi.org/packages/c7/6d/46ea318a905108c90dd1f2f9766e4c85a8059f9796b4e3a407c699de3839/hatchet-0.0.3.tar.gz")
    version("0.0.2", sha256="2ac90e31b2488d53e27e51557a0224740c9ed965c6dd8c3e8d6b25a5225c545d", url="https://pypi.org/packages/56/e8/7a716e59cf106b932c4204b9cd7d4f05cb1e464c3a74326f19d213ffc994/hatchet-0.0.2.tar.gz")
    version("0.0.1", sha256="e21182684d2d7cc2d0357b46b501c8c1164aa2941994d755a5487d2a1ca53c31", url="https://pypi.org/packages/30/72/6b0a5c9bbf2c19cce616999fe85520b184b54c6f9e9a567e11176a1e41e4/hatchet-0.0.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-matplotlib", when="@1.2")
        depends_on("py-numpy", when="@1.2")
        depends_on("py-pandas", when="@1.2")
        depends_on("py-pydot", when="@1.2")
        depends_on("py-pyyaml", when="@1.2")

