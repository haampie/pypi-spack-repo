# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonJose(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.3.0", sha256="9b1376b023f8b298536eedd47ae1089bcdb848f1535ab30555cd92002d78923a", url="https://pypi.org/packages/bd/2d/e94b2f7bab6773c70efc70a61d66e312e1febccd9e0db6b9e0adf58cbad1/python_jose-3.3.0-py2.py3-none-any.whl")
    version("3.2.0", sha256="67d7dfff599df676b04a996520d9be90d6cdb7e6dd10b4c7cacc0c3e2e92f2be", url="https://pypi.org/packages/2b/55/bc3e9a4013a50287ec30e653c85cd10f077f8bca73bcda869847bf18cf37/python_jose-3.2.0-py2.py3-none-any.whl")
    version("3.1.0", sha256="1ac4caf4bfebd5a70cf5bd82702ed850db69b0b6e1d0ae7368e5f99ac01c9571", url="https://pypi.org/packages/6c/80/5bdf2543fe002dc74429e9360148deb4d9e0b453acdc2b5c6fb1617f4f9d/python_jose-3.1.0-py2.py3-none-any.whl")
    version("3.0.1", sha256="29701d998fe560e52f17246c3213a882a4a39da7e42c7015bcc1f7823ceaff1c", url="https://pypi.org/packages/96/da/c0dcc5e7a98a53440b8db3cf9771345fa696754f79e8734ea59123f7d734/python_jose-3.0.1-py2.py3-none-any.whl")
    version("3.0.0", sha256="e06dd2e5e9125da79b519ff2652b8c666d64a5ea228fcd9862e0b29a534ccc53", url="https://pypi.org/packages/44/5b/c8adb4d8052b2c7ced00888e1cd7b2b18d0493019faf0163617bdbde59d8/python_jose-3.0.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-ecdsa@:0.14,0.16:", when="@3.3:")
        depends_on("py-ecdsa@:0.14", when="@3.2")
        depends_on("py-pyasn1", when="@3.2:")
        depends_on("py-rsa", when="@3.2:")
        depends_on("py-six", when="@3.2")
    # END DEPENDENCIES

