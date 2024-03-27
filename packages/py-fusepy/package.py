##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFusepy(PythonPackage):
    version("3.0.1", sha256="72ff783ec2f43de3ab394e3f7457605bf04c8cf288a2f4068b4cde141d4ee6bd", url="https://pypi.org/packages/04/0b/4506cb2e831cea4b0214d3625430e921faaa05a7fb520458c75a2dbd2152/fusepy-3.0.1.tar.gz")
    version("2.0.4", sha256="a9f3a3699080ddcf0919fd1eb2cf743e1f5859ca54c2018632f939bdfac269ee", url="https://pypi.org/packages/79/87/22d2cf8445093fc8c7f25952bdbc505ec175c00942ffa29d23b60097ecf1/fusepy-2.0.4.zip")


