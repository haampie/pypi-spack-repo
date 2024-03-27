##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOutdated(PythonPackage):
    version("0.2.2", sha256="3e9c2ee6d17e86ae8cc7bb71d70c4172690121cda367155a30994742172678c8", url="https://pypi.org/packages/d3/04/7d2b9a0d1b81e30f39e6f358bac01f4f18b585f35b0ffc5c83fc274f146b/outdated-0.2.2-py2.py3-none-any.whl")
    version("0.2.1", sha256="177e381857c10c410dc643b48ace8753ab977d5ae39642297a7f76eb4a3c1c8e", url="https://pypi.org/packages/fd/f6/95588d496e518355c33b389222c99069b1c6f2c046be64f400072fdc7cda/outdated-0.2.1-py3-none-any.whl")
    version("0.2.0", sha256="bcb145e0e372ba467e998c327d3d1ba72a134b0d5a729749729df6c6244ce643", url="https://pypi.org/packages/86/70/2f166266438a30e94140f00c99c0eac1c45807981052a1d4c123660e1323/outdated-0.2.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-littleutils", when="@0.2.1:")
        depends_on("py-requests", when="@0.2.1:")
        depends_on("py-setuptools@44:", when="@0.2.2:")

