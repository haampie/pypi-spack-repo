# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCliff(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("4.6.0", sha256="58a90e87738b9a7df672a5f9627bcd668564d01d8e567170dfe2d3a0026adb31", url="https://pypi.org/packages/e4/71/8506c160225ac44041eb1edcd90dd456878a41915c130b6b854f5eb31ef6/cliff-4.6.0-py3-none-any.whl")
    version("4.5.0", sha256="0cb50f41e13fb90d32e5a66969966427cbbef98ef397cef4eb78bfad52ef747c", url="https://pypi.org/packages/31/f8/b9989a872192ded4775349abefd32cad60868852a8f892eff3af30be41f8/cliff-4.5.0-py3-none-any.whl")
    version("4.4.0", sha256="bcad956095df58956eb6931cbfd99cae607d0dd516c9669b3967e77800ce920d", url="https://pypi.org/packages/61/fe/94926a6fa959cb0f7d06848cb7b04b08156c561e67a6fd7dc82e6073fd7e/cliff-4.4.0-py3-none-any.whl")
    version("4.3.0", sha256="db3dc8774f47db9aa86796921ff158d0f023630261c2746c4fff12584b75f5b2", url="https://pypi.org/packages/d0/4a/8f88349df1a7069689ec88c4aa0d2cb08740246803629eda96aaf917a796/cliff-4.3.0-py3-none-any.whl")
    version("4.2.0", sha256="5538a03299f40f83268ba102ed513c2a693ffeb6ac01de7cc119ae9cfc55e55d", url="https://pypi.org/packages/1c/43/9b457121d6b408df41468382497ec3abd1023facaee21e1407aa28570466/cliff-4.2.0-py3-none-any.whl")
    version("4.1.0", sha256="99a98ef89cc19b2970be4de94a266217c6e0729c6b80145865af449c9032a0e3", url="https://pypi.org/packages/43/f1/945898cefac8bccbfb8ab0e344dce4420384c21f2cabee7868af318196ca/cliff-4.1.0-py3-none-any.whl")
    version("4.0.0", sha256="3f28b95a5509b4c7f0dd17dac7495018bd08a84edde93386e10236751900064b", url="https://pypi.org/packages/f8/f2/512d5d95cae0ae7fab664cd9114575564976834dbec0d5bea229e0b2e170/cliff-4.0.0-py3-none-any.whl")
    version("3.10.1", sha256="a21da482714b9f0b0e9bafaaf2f6a8b3b14161bb47f62e10e28d2fe4ff4b1626", url="https://pypi.org/packages/a3/9d/3678f7a6278d9d8908df1de6c110fd1bd0e5cadcb63b82c1c7c0a90d227c/cliff-3.10.1-py3-none-any.whl")
    version("3.10.0", sha256="86ce931944c56a86094fef82c216d2342f42ee21e21bea376c1ece82fc6ae49a", url="https://pypi.org/packages/19/80/d1b21a80864c6386c72d69de2e343188f3d97f7ab5646525c43f0e72b6fb/cliff-3.10.0-py3-none-any.whl")
    version("3.9.0", sha256="c0d02ee970f978becf04ac7c2a921f2edbde83b1f1b5a7b7e0500e63fd9a6ca7", url="https://pypi.org/packages/18/f7/2a98b032a43b2925ea32bc13a8feb6cf9416e7d2b2c0f6d2ce14636a03b1/cliff-3.9.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-autopage@0.4:", when="@3.9:")
        depends_on("py-cmd2@1:", when="@3.7:")
        depends_on("py-importlib-metadata@4.4:", when="@4.5: ^python@:3.9")
        depends_on("py-importlib-metadata@4.4:", when="@4:4.4")
        depends_on("py-pbr@2:2.0,3:", when="@2.6:3")
        depends_on("py-prettytable@0.7.2:", when="@3.7:")
        depends_on("py-pyparsing@2.1:", when="@2.4.1:3")
        depends_on("py-pyyaml@3.12:", when="@2.12:2.16,2.18:")
        depends_on("py-stevedore@2.0.1:", when="@3.4:")
    # END DEPENDENCIES

