# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLlnlSina(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.11.0", sha256="a9891e8b050df40c5145d53eb5daf7ee622854a0e26876e1643463d6665f561e", url="https://pypi.org/packages/f1/f7/3b3ec3791e5b0198a195a57b427473801e0f8776e23307fc5b6b95a6c5b9/llnl_sina-1.11.0-py2.py3-none-any.whl")
    version("1.10.0", sha256="70b84738d1ae2a1bda988c1b508c5e32867ce75b5460fce5d5e941e377e6d0a5", url="https://pypi.org/packages/39/d9/faf441dcaba99567f8804516f0faf37de726d4cc65b5f1454153ddec615e/llnl_sina-1.10.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-six")
        depends_on("py-sqlalchemy", when="@:1.13")
    # END DEPENDENCIES


        # marker: python_version >= "3.6" and platform_machine != "ppc64le"
        # depends_on("py-orjson", when="@1.10:")

        # marker: python_version >= "3.6" and platform_machine == "ppc64le"
        # depends_on("py-ujson", when="@1.10:")
