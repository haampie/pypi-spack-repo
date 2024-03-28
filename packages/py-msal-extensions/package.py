# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMsalExtensions(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.1.0", sha256="01be9711b4c0b1a151450068eeb2c4f0997df3bba085ac299de3a66f585e382f", url="https://pypi.org/packages/78/8d/ecd0eb93196f25c722ba1b923fd54d190366feccfa5b159d48dacf2b1fee/msal_extensions-1.1.0-py3-none-any.whl")
    version("1.0.0", sha256="91e3db9620b822d0ed2b4d1850056a0f133cba04455e62f11612e40f5502f2ee", url="https://pypi.org/packages/52/34/a8995d6f0fa626ff6b28dbd9c90f6c2a46bd484bc7ab343d078b0c6ff1a7/msal_extensions-1.0.0-py2.py3-none-any.whl")
    version("0.3.1", sha256="89df9c0237e1adf16938fa58575db59c2bb9de04a83ffb0452c8dfc79031f717", url="https://pypi.org/packages/f2/26/76c71350c84bf42740a5cec20b428c77219abf2e251a1be31056952bb0de/msal_extensions-0.3.1-py2.py3-none-any.whl")
    version("0.3.0", sha256="a530c2d620061822f2ced8e29da301bc928b146970df635c852907423e8ddddc", url="https://pypi.org/packages/49/cb/c833ffa0f97c3098b146ac19bb2266c2d84b2119ffff83fdf001bb59d3ae/msal_extensions-0.3.0-py2.py3-none-any.whl")
    version("0.2.2", sha256="f092246787145ec96d6c3c9f7bedfb837830fe8a79b56180e531fbf28b8de532", url="https://pypi.org/packages/33/da/eed514cb6902405c5c11a03f1e65adbd95e2c26d9b22eae390eddb561201/msal_extensions-0.2.2-py2.py3-none-any.whl")
    version("0.1.3", sha256="c5a32b8e1dce1c67733dcdf8aa8bebcff5ab123e779ef7bc14e416bd0da90037", url="https://pypi.org/packages/21/9b/8bc67822e98573fe0460e30ad0202ab9e0638a42878041c65a6fe857babe/msal_extensions-0.1.3-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-msal@0.4.1:", when="@0.1.3:")
        depends_on("py-packaging", when="@1.1:")
        depends_on("py-portalocker@1.6:", when="@0.3.1: platform=windows")
        depends_on("py-portalocker@1:", when="@0.3.1: platform=linux")
        depends_on("py-portalocker@1:", when="@0.3.1: platform=freebsd")
        depends_on("py-portalocker@1:", when="@0.3.1: platform=darwin")
        depends_on("py-portalocker@1:", when="@0.3.1: platform=cray")
        depends_on("py-portalocker@1.6:1", when="@0.2.1:0.3.0 platform=windows")
        depends_on("py-portalocker@1", when="@0.2.1:0.3.0 platform=linux")
        depends_on("py-portalocker@1", when="@0.2.1:0.3.0 platform=freebsd")
        depends_on("py-portalocker@1", when="@0.2.1:0.3.0 platform=darwin")
        depends_on("py-portalocker@1", when="@0.2.1:0.3.0 platform=cray")
        depends_on("py-portalocker@1.6:1", when="@0.2:0.2.0")
        depends_on("py-portalocker@1", when="@:0.1")
    # END DEPENDENCIES

