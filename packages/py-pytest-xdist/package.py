##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestXdist(PythonPackage):
    version("3.2.0", sha256="336098e3bbd8193276867cc87db8b22903c3927665dff9d1ac8684c02f597b68", url="https://pypi.org/packages/e5/62/78212674a3fab3e15c81812a3889480ed5ac4c82b1ab9c37c74834f30920/pytest_xdist-3.2.0-py3-none-any.whl")
    version("1.30.0", sha256="a8569b027db70112b290911ce2ed732121876632fb3f40b1d39cd2f72f58b147", url="https://pypi.org/packages/f7/80/2af1fc039f779f61c7207dc9f79a1479874e7795f869fddaf135efde1cd4/pytest_xdist-1.30.0-py2.py3-none-any.whl")
    version("1.29.0", sha256="501795cb99e567746f30fe78850533d4cd500c93794128e6ab9988e92a17b1f8", url="https://pypi.org/packages/9f/cc/371b2e6dfbf4e8df07b04e310dd6ea0b3f367e257d1e6cb516b25bc4af1b/pytest_xdist-1.29.0-py2.py3-none-any.whl")
    version("1.27.0", sha256="a64915be2b23235d6cec0992b8f59b791d64083756fbf13cf574fa5757085bc7", url="https://pypi.org/packages/fe/1f/508b18176dc2ea51008f8f811751ab69db5d2f105fbfb36ea935f3f68da2/pytest_xdist-1.27.0-py2.py3-none-any.whl")
    version("1.24.0", sha256="3bc9dcb6ff47e607d3c710727cd9996fd7ac1466d405c3b40bb495da99b6b669", url="https://pypi.org/packages/1b/92/a45a140b4024988f65eb76020101fa6da968b43716121595452b8bafb506/pytest_xdist-1.24.0-py2.py3-none-any.whl")
    version("1.17.0", sha256="e7e48c111677af23078b1ed23501e493e12c4b6d91657f6884a64e4ce0f14144", url="https://pypi.org/packages/ab/92/4c4ee42cd590b628193efa73868a02e5cda98a583d28602f87dddec3ca55/pytest-xdist-1.17.0.tar.gz")
    version("1.16.0", sha256="42e5a1e5da9d7cff3e74b07f8692598382f95624f234ff7e00a3b1237e0feba2", url="https://pypi.org/packages/0d/d0/58cacddb34f35dd3d447525061e431b00d842eef72d585cc1c9a97abec90/pytest-xdist-1.16.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-execnet@1.1:", when="@:0,1.13,1.20.1:")
        depends_on("py-psutil@3:", when="@2:2.0")
        depends_on("py-pytest@4.4:", when="@1.28:1")
        depends_on("py-pytest@3.6:", when="@1.25:1.27")
        depends_on("py-pytest@3:", when="@1.20.1:1.22.3,1.22.5:1.24")
        depends_on("py-pytest@6.2:", when="@:0,2.5:")
        depends_on("py-pytest-forked", when="@1.20.1:2")
        depends_on("py-six", when="@1.22.5:1")

