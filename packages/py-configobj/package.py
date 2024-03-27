##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyConfigobj(PythonPackage):
    version("5.0.8", sha256="a7a8c6ab7daade85c3f329931a807c8aee750a2494363934f8ea84d8a54c87ea", url="https://pypi.org/packages/d3/bb/d10e531b297dd1d46f6b1fd11d018247af9f2d460037554bb7bb9011c6ac/configobj-5.0.8-py2.py3-none-any.whl")
    version("5.0.7", sha256="f60743cfa2f58d3e830e0c19a0b6864d845e9b9622ec416126c792de0de40b6d", url="https://pypi.org/packages/90/11/28e9678700acd4a50e2ecec7eee2614e0f57e1ca70ddee70168241728c27/configobj-5.0.7-py2.py3-none-any.whl")
    version("5.0.6", sha256="a2f5650770e1c87fb335af19a9b7eb73fc05ccf22144eb68db7d00cd2bcb0902", url="https://pypi.org/packages/64/61/079eb60459c44929e684fa7d9e2fdca403f67d64dd9dbac27296be2e0fab/configobj-5.0.6.tar.gz")
    version("4.7.2", sha256="515ff923462592e8321df8b48c47e3428f8d406ee22b8de77bef969d1af11171", url="https://pypi.org/packages/49/9c/4a97c36ba82e60b390614f050cd1d3e8652f1b38d1e6fde6e1ff4f16bc3e/configobj-4.7.2.tar.gz")

    with default_args(type="run"):
        depends_on("py-six", when="@5.0.7:")

