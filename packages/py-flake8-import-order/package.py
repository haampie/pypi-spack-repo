# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFlake8ImportOrder(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.18.2", sha256="82ed59f1083b629b030ee9d3928d9e06b6213eb196fe745b3a7d4af2168130df", url="https://pypi.org/packages/0c/52/9c5cb50a61f3d90f9d6c98ba67e3227f4057dc398cf664f3b56cb7c261f7/flake8_import_order-0.18.2-py2.py3-none-any.whl")
    version("0.18.1", sha256="90a80e46886259b9c396b578d75c749801a41ee969a235e163cfe1be7afd2543", url="https://pypi.org/packages/ab/52/cf2d6e2c505644ca06de2f6f3546f1e4f2b7be34246c9e0757c6048868f9/flake8_import_order-0.18.1-py2.py3-none-any.whl")
    version("0.18", sha256="feca2fd0a17611b33b7fa84449939196c2c82764e262486d5c3e143ed77d387b", url="https://pypi.org/packages/9c/59/f3028e0a02e714997aca57c5936cc6b2a0a35d5c809bef7421c8563800a2/flake8_import_order-0.18-py2.py3-none-any.whl")
    version("0.17.1", sha256="40d2a39ed91e080f3285f4c16256b252d7c31070e7f11b7854415bb9f924ea81", url="https://pypi.org/packages/fc/e7/f029c699da3c9dd2e7635bd23374c76d0f906abb77a7677e9221f85205e2/flake8_import_order-0.17.1-py2.py3-none-any.whl")
    version("0.17", sha256="d605fd3de61fd76492ee06f031021b19278aa9ce1f92d128930475e1efb71cae", url="https://pypi.org/packages/cb/75/edb8dd9842775a1d5a02addadb83effc0abfb3b3b7c97f1276931f1ddc8f/flake8_import_order-0.17-py2.py3-none-any.whl")
    version("0.16", sha256="e85c19bf515edecb993e971ed286c3cdd7139b289c10300843528503de0b8c4e", url="https://pypi.org/packages/92/36/c53e47a828fae5fb04ad5cbef40b8b4f4c51d025a77d32753ef9dadc1304/flake8_import_order-0.16-py2.py3-none-any.whl")
    version("0.15", sha256="68edbbf4089af57bd303ff51bb2aa2df24d266c23308db3e6b47357d1f80ad60", url="https://pypi.org/packages/6c/a4/68056e3d6ebf820970ddcad5fe0271a5c0723799ed3df7b002a9c5842fb1/flake8_import_order-0.15-py2.py3-none-any.whl")
    version("0.14.3", sha256="26c052d93d8b2d17c5e31bdcf0cdcb513c0b039d2671905dc9ddb5bcec8f72e1", url="https://pypi.org/packages/80/8f/9f69326562f05e47f6102d648f85eb09e4a81ca97615c83b5a69a141bdfa/flake8_import_order-0.14.3-py2.py3-none-any.whl")
    version("0.14.2", sha256="3351e102c4702391ba86d2acf22a0b2170336288193714dcc245d1ab9f0548f0", url="https://pypi.org/packages/c0/7c/55a641df1a9990a7f930600dccfa4128535172e9ae7c91420000fa2d6005/flake8_import_order-0.14.2-py2.py3-none-any.whl")
    version("0.14.1", sha256="d8b5e1144224e673551c4d96ddce6a7d518a72792e868eacde1fceb0fc332bae", url="https://pypi.org/packages/ab/f4/c9aef38ae757a511bb086d180cf686067c8b0cb75e7deb6feb23b028eab6/flake8_import_order-0.14.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-asttokens", when="@0.14.1:0.15")
        depends_on("py-enum34", when="@0.17:0.17.0")
        depends_on("py-pycodestyle", when="@0.9:")
        depends_on("py-setuptools", when="@0.12:")
    # END DEPENDENCIES

