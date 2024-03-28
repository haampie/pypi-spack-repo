# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLlnlSina(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.14.0", sha256="099e484b016ddadda579cda85a0a3b612b15a458caaf07285b5fa8fdbd4f4c0d", url="https://pypi.org/packages/03/75/9e97c22775442b1841b8008965a06307b2a052072bcc6c336282edd7e316/llnl_sina-1.14.0-py2.py3-none-any.whl")
    version("1.13.0", sha256="78826d835cd08a75f474afd10268d0deeefa9213a068649aef7d143e55ffc113", url="https://pypi.org/packages/be/a3/2a5e7d86c9d4958c3ae07bd7e7b2ae0754962d9e418e5a18bfad363b349e/llnl_sina-1.13.0-py2.py3-none-any.whl")
    version("1.12.0", sha256="71647f6baee82cf2a345a29e626e9248ed46f074dd692c033e55a6d8ed2e4d7b", url="https://pypi.org/packages/44/58/528f8d1095fc01057ec9d39540a433aeb5f5f811068fe2fc34a07be5c204/llnl_sina-1.12.0-py2.py3-none-any.whl")
    version("1.11.0", sha256="a9891e8b050df40c5145d53eb5daf7ee622854a0e26876e1643463d6665f561e", url="https://pypi.org/packages/f1/f7/3b3ec3791e5b0198a195a57b427473801e0f8776e23307fc5b6b95a6c5b9/llnl_sina-1.11.0-py2.py3-none-any.whl")
    version("1.10.0", sha256="70b84738d1ae2a1bda988c1b508c5e32867ce75b5460fce5d5e941e377e6d0a5", url="https://pypi.org/packages/39/d9/faf441dcaba99567f8804516f0faf37de726d4cc65b5f1454153ddec615e/llnl_sina-1.10.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-freetype-py", when="@1.13: platform=darwin")
        depends_on("py-six")
        depends_on("py-sqlalchemy@:1", when="@1.14:")
        depends_on("py-sqlalchemy", when="@:1.13")

        # marker: python_version >= "3.6" and platform_machine != "ppc64le"
        # depends_on("py-orjson", when="@1.10:")

        # marker: python_version >= "3.6" and platform_machine == "ppc64le"
        # depends_on("py-ujson", when="@1.10:")
    # END DEPENDENCIES

