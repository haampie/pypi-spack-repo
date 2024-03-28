# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPlotly(PythonPackage):
    # BEGIN VERSIONS
    version("5.20.0", sha256="837a9c8aa90f2c0a2f0d747b82544d014dc2a2bdde967b5bb1da25b53932d1a9", url="https://pypi.org/packages/00/4e/6258fc3b26f1f7abd1b2e75b1e9e4f12f13584136e2e1549f995ff4c6b7b/plotly-5.20.0-py3-none-any.whl")
    version("5.19.0", sha256="906abcc5f15945765328c5d47edaa884bc99f5985fbc61e8cd4dc361f4ff8f5a", url="https://pypi.org/packages/27/ae/c9fb759b36bc55ccc382b647d1afc23c2a860be8e835f96249996d0aa4df/plotly-5.19.0-py3-none-any.whl")
    version("5.18.0", sha256="23aa8ea2f4fb364a20d34ad38235524bd9d691bf5299e800bca608c31e8db8de", url="https://pypi.org/packages/a8/07/72953cf70e3bd3a24cbc3e743e6f8539abe6e3e6d83c3c0c83426eaffd39/plotly-5.18.0-py3-none-any.whl")
    version("5.17.0", sha256="7c84cdf11da162423da957bb093287134f2d6f170eb9a74f1459f825892247c3", url="https://pypi.org/packages/df/79/c80174d711ee26ee5da55a9cc3e248f1ec7a0188b5e4d6bbbbcd09b974b0/plotly-5.17.0-py2.py3-none-any.whl")
    version("5.16.1", sha256="19cc34f339acd4e624177806c14df22f388f23fb70658b03aad959a0e650a0dc", url="https://pypi.org/packages/26/5d/1e13b597ed8e54803e9ac6ded18c04cd35d8cbc49016778ec50c4ca9e9d5/plotly-5.16.1-py2.py3-none-any.whl")
    version("5.16.0", sha256="046ba0cd9f6b251780e0d93313016ec5e2cb69d9a68da818cd7110e6c77a4011", url="https://pypi.org/packages/d6/54/a8759957b778094233d7058c8ddbe368504b448ffe9c26a85f7bfd53584e/plotly-5.16.0-py2.py3-none-any.whl")
    version("5.15.0", sha256="3508876bbd6aefb8a692c21a7128ca87ce42498dd041efa5c933ee44b55aab24", url="https://pypi.org/packages/a5/07/5bef9376c975ce23306d9217ab69ca94c07f2a3c90b17c03e3ae4db87170/plotly-5.15.0-py2.py3-none-any.whl")
    version("5.14.1", sha256="a63f3ad9e4cc2e02902a738e5e3e7f3d1307f2732ac71a6c28f1238ed3052826", url="https://pypi.org/packages/15/5c/786e4572cf3217ba1707eeb99fe4bdb8fb138237690fa21641e341b1970c/plotly-5.14.1-py2.py3-none-any.whl")
    version("5.14.0", sha256="2e3407d93a9700beebbef66d11f63992c58e058dd808442ee54af40f98fb4940", url="https://pypi.org/packages/78/06/716dfc518422911c6c8863d4008b30401bb0c2cb20c7a2e5f910f25d3d1b/plotly-5.14.0-py2.py3-none-any.whl")
    version("5.13.1", sha256="f776a5c664908450c6c1727f61e8e2e22798d9c6c69d37a9057735365084a2fa", url="https://pypi.org/packages/f7/f5/c5b30c0a6639f076615d56f628f507ae20388e8f8769aef99ce5ea2033c8/plotly-5.13.1-py2.py3-none-any.whl")
    version("5.2.2", sha256="25ad75f8944c950b01811b4521f39104ce0ede92ebf7821aef74ba6530a63fab", url="https://pypi.org/packages/79/d2/2e1fecbfe211edd0ad188e895a01f03e6ffd636639d7344b316ed7606d68/plotly-5.2.2-py2.py3-none-any.whl")
    version("2.2.0", sha256="ca668911ffb4d11fed6d7fbb12236f8ecc6a7209db192326bcb64bdb41451a58", url="https://pypi.org/packages/55/ec/470525656ec15dc6907bf70d9b9630bd518364eef21b3c73bf7a40ca0474/plotly-2.2.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-packaging", when="@5.14:")
        depends_on("py-six", when="@3.1.1-rc1:3.1,3.2.0-alpha2:3.6.0-rc1,3.6.1:5.7")
        depends_on("py-tenacity@6.2:", when="@5:")
    # END DEPENDENCIES

