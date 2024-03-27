##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPykwalify(PythonPackage):
    version("1.8.0", sha256="731dfa87338cca9f559d1fca2bdea37299116e3139b73f78ca90a543722d6651", url="https://pypi.org/packages/1f/fd/ac2161cce19fd67a18c269073f8e86292b5511acec6f8ef6eab88615d032/pykwalify-1.8.0-py2.py3-none-any.whl")
    version("1.7.0", sha256="428733907fe5c458fbea5de63a755f938edccd622c7a1d0b597806141976f00e", url="https://pypi.org/packages/36/9f/612de8ca540bd24d604f544248c4c46e9db76f6ea5eb75fb4244da6ebbf0/pykwalify-1.7.0-py2.py3-none-any.whl")
    version("1.6.1", sha256="191fd3f457f23c0aa8538c3a5c0249f70eeb1046e88d0eaaef928e09c44dff8d", url="https://pypi.org/packages/c9/43/84d3b52161d27f7168c5870c79b97255f9d01c4b259bf32ca42dd39c21f0/pykwalify-1.6.1.tar.gz")
    version("1.6.0", sha256="2298fafe84dc68161835f62a1b8d0d72dd749d5742baa196224882a6ac2ff844", url="https://pypi.org/packages/ae/82/1774cdd9039301f20e36ae5bf36fa07683ac2d0c42a3d51cf3e0690210c1/pykwalify-1.6.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-docopt@0.6.2:", when="@1.7:")
        depends_on("py-python-dateutil@2.8:", when="@1.8:")
        depends_on("py-python-dateutil@2.4.2:", when="@1.7")
        depends_on("py-pyyaml@3.11:", when="@1.7")
        depends_on("py-ruamel-yaml@0.16:", when="@1.8:")

