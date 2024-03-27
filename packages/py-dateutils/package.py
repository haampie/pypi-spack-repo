##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDateutils(PythonPackage):
    version("0.6.12", sha256="f33b6ab430fa4166e7e9cb8b21ee9f6c9843c48df1a964466f52c79b2a8d53b3", url="https://pypi.org/packages/1e/23/cbac954194e5132448cfec0148be1318baac99e68ed597b3d7ff4ae5c182/dateutils-0.6.12-py2.py3-none-any.whl")
    version("0.6.11", sha256="8effff2ca5550335d7fdff4de9072a8e14f2b466d8f4b209761aee548842b66b", url="https://pypi.org/packages/5e/bf/e68c863e72fbf19c84841cdc0d2719ce1741c2ae004f133af9cb3fba3adc/dateutils-0.6.11-py2.py3-none-any.whl")
    version("0.6.10", sha256="969ce05cfac359592f28205949a84c81db26b5fd8ec8378118c871b6ae1c74b8", url="https://pypi.org/packages/b0/a3/9700f62fe91136e4716e9eef995885f51bc3194fb70013b52fd26d975e3d/dateutils-0.6.10-py2.py3-none-any.whl")
    version("0.6.9", sha256="c189270a35e4607044e25f9c715932df3b26d4780a88e36e32138ceb74cf52db", url="https://pypi.org/packages/01/2a/2a23324adecceb3a6fd341c630408ce0a859b645f8675d276b078b888ffc/dateutils-0.6.9-py2.py3-none-any.whl")
    version("0.6.8", sha256="15e564d9cd34e4260cf96625a3249c938c3aada2e5eaddf8218dd3fbc8dbdba4", url="https://pypi.org/packages/9f/33/059126d2e2f5f28c2f547d36f38078c620444d8378e5b371e77ff4ae6b6d/dateutils-0.6.8.tar.gz")
    version("0.6.7", sha256="98ba55b20306450768e06aa9dbcd75105384c2c39a3060702144ed518716cb49", url="https://pypi.org/packages/9d/cd/50844be53eac7e0a4d3a8e4f22a64e90c65ad9fa7d06dc5de55503d4486c/dateutils-0.6.7.tar.gz")
    version("0.6.6", sha256="c94a8e77d743abac79ed91f99f5ef594a972a527e05145cbb7aba59beced8a71", url="https://pypi.org/packages/5b/11/246237ce2a1dd87ffebef0e430033f877b31dd208b281914d4fd3c531ee7/dateutils-0.6.6.tar.gz")

    with default_args(type="run"):
        depends_on("py-argparse", when="@0.6.9:0.6.11")
        depends_on("py-python-dateutil", when="@0.6.9:")
        depends_on("py-pytz", when="@0.6.9:")

