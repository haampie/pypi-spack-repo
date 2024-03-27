##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkOslog(PythonPackage):
    version("10.2", sha256="2377637a0de7dd60f610caab4bcd7efa165d23dba4ac896fd542f1fab2fc588a", url="https://pypi.org/packages/ef/76/f808e7ca93f38a2552329e3eca85b2047910e61d12f1b3ceb7b7a752fd5e/pyobjc-framework-OSLog-10.2.tar.gz")
    version("10.1", sha256="bfce0067351115ae273489768f93692dcda88bd5b54f28bb741c08855c114dfe", url="https://pypi.org/packages/ee/fc/512f87b289a4c905eda08210345e590d0e6ebefd215dbbace9cef0deac67/pyobjc-framework-OSLog-10.1.tar.gz")
    version("10.0", sha256="3a169df2fe5fdbd6ca8db28e5c51d89f8759b369636ea7cc2672cde11f4a09fb", url="https://pypi.org/packages/f8/c3/3c2f53709b3e36c5b8d5acad109b8fea6d52a69f758c40a8129444907318/pyobjc-framework-OSLog-10.0.tar.gz")
    version("9.2", sha256="08c05011c99308ce7591213cc9133029717483c9b3484c234d73fd5bacbd6fd2", url="https://pypi.org/packages/d3/56/db71d1eee0de501cbe3f1c5b493cb7135726c34eade5b9cdd9f097580d31/pyobjc-framework-OSLog-9.2.tar.gz")
    version("9.1.1", sha256="35361d31d5d0f1e33f4f6ae8794a0c5da1cbd5f3027fe69d1c1b853ea282965b", url="https://pypi.org/packages/54/98/12a4f38b1d243dfaad071fa8b0871e80d29aa22878f3b320e3ec95e99758/pyobjc-framework-OSLog-9.1.1.tar.gz")
    version("9.1", sha256="2cacd7bc1ed59a1490aeb8d47e9431cd5d1ab72e3c29df178a1ad38752ec6c8a", url="https://pypi.org/packages/75/5c/b52af67b4deafd94f6ddd75d1eeab5c04837afe80ce98251c859babef85e/pyobjc-framework-OSLog-9.1.tar.gz")
    version("9.0.1", sha256="964499ffc06ba3b347ef8a96d99a882ee5b5abdbc55c17722344c1d4535ec4f9", url="https://pypi.org/packages/60/5f/84089542c1fef3ac85dc740798eb875d9feddfb2c999103ac138b2d3f095/pyobjc-framework-OSLog-9.0.1.tar.gz")
    version("9.0", sha256="47f99ebd1160451c6586182c45ae7a8bf6e26131b5c39ca4140f2dfa0e3f713e", url="https://pypi.org/packages/f7/1d/7b3f4219c297944725b7f63637d1102f0a72f6afdba8a056f5c7e88aafa2/pyobjc-framework-OSLog-9.0.tar.gz")
    version("8.5.1", sha256="a770e6bea5464e42e91e361f56fbd5ebcad9bcde0a06d0d63328409bfc2fa3a1", url="https://pypi.org/packages/06/f6/f43833f1a78654e3844f97c9febd50aa3b05fe0b5bdd9a5a87ea59295f40/pyobjc-framework-OSLog-8.5.1.tar.gz")
    version("8.5", sha256="63551865ca3554f0f85cb3a7799b2471c0f89146b23cb12e939dad7d11c9e08a", url="https://pypi.org/packages/d9/a3/2eeb5ab645bd3f8b3b1be4bbfddd5003b4ce1c7e99e6aa5e0be7d64f6d4b/pyobjc-framework-OSLog-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-coremedia@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coremedia@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-coremedia@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-quartz@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-quartz@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-quartz@10:", when="@10:10.0")

