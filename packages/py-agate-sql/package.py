##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAgateSql(PythonPackage):
    version("0.7.2", sha256="be1cb9a99b3e4ec7f6106278dfb7b534be9629c8a983abb168c3effacc79dd10", url="https://pypi.org/packages/42/41/ce4192b0ee21d5120d20de58751ce56fae7bebe4c56966dc64c41534d4e4/agate_sql-0.7.2-py2.py3-none-any.whl")
    version("0.7.1", sha256="24416a93d2b2f5a0a7e1f09b4f6b1d61f04c54f071f1d06f70f6fcfacfd2bf6e", url="https://pypi.org/packages/b7/20/9a1e3c6f5a745b0d5050665b13fe5b387af96c5a2a7e2f717bfabbab1768/agate_sql-0.7.1-py2.py3-none-any.whl")
    version("0.7.0", sha256="176972152095e2a1cbc283d3c07bac3c59270288ab572a1dab5619e87ed93f2f", url="https://pypi.org/packages/ea/bf/96ad8b8d673d35b3f237490726e5602082ad21e7e2b0416bc1086c3a0901/agate_sql-0.7.0-py2.py3-none-any.whl")
    version("0.6.0", sha256="58377c3d7a63613f6a7a0188f0f27a3fc1dad78ac375fe1231c36dd67fc3632e", url="https://pypi.org/packages/e0/13/a99ebff890aef80110cfad64830bdf8f20bde48f02d00a4500ab064954af/agate_sql-0.6.0-py2.py3-none-any.whl")
    version("0.5.9", sha256="de199dc5863775fe813b139ec7357f309aab8fd785ae8ee456ad07ee4e24a0e0", url="https://pypi.org/packages/f8/94/50a755327d54b8863dce982bb5d3e9c4558729735829a199ef68e9852e58/agate_sql-0.5.9-py2.py3-none-any.whl")
    version("0.5.8", sha256="aae3d1014c3396cb0c21a21f0e41b514128bc0479b9a1627d020611f470199c3", url="https://pypi.org/packages/f9/ea/b99b9f12dd4438907c9d6e18fd226f58a9321011fabffe0a8f80c3bf64ea/agate_sql-0.5.8-py2.py3-none-any.whl")
    version("0.5.7", sha256="a4fccbc4df21c3dd885d5a48c20c237815bb96d7eead2fd95917c16a30d18afa", url="https://pypi.org/packages/30/84/e8c138b58ad5c00a0ec996aedb874564232f44b957578802e30a7d75cb62/agate_sql-0.5.7-py2.py3-none-any.whl")
    version("0.5.6", sha256="056dc9e587fbdfdf3f1c9950f4793a5ee87622c19deba31aa0a6d6681816dcde", url="https://pypi.org/packages/f2/97/261281b84bbb35502d29e39da2f1f0ee3d5d08bd982e48fcb8294b69a0e7/agate-sql-0.5.6.tar.gz")
    version("0.5.5", sha256="50a39754babef6cd0d1b1e75763324a49593394fe46ab1ea9546791b5e6b69a7", url="https://pypi.org/packages/72/f4/c029cedda61bc9d3cca80a601c8f1960ddd7fce66776da7f298557172fc1/agate-sql-0.5.5.tar.gz")
    version("0.5.4", sha256="9277490ba8b8e7c747a9ae3671f52fe486784b48d4a14e78ca197fb0e36f281b", url="https://pypi.org/packages/4a/fb/796c6e7b625fde74274786da69f08aca5c5eefb891db77344f95ad7b75db/agate-sql-0.5.4.tar.gz")

    with default_args(type="run"):
        depends_on("py-agate@1.5:", when="@0.5.7:")
        depends_on("py-sqlalchemy@1.4.0:", when="@0.6:")
        depends_on("py-sqlalchemy@:1", when="@0.5.9:0.5")
        depends_on("py-sqlalchemy@1.0.8:", when="@0.5.7:0.5.8")

