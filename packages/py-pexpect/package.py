# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPexpect(PythonPackage):
    # BEGIN VERSIONS
    version("4.8.0", sha256="0b48a55dcb3c05f3329815901ea4fc1537514d6ba867a152b581d69ae3710937", url="https://pypi.org/packages/39/7b/88dbb785881c28a102619d46423cb853b46dbccc70d3ac362d99773a78ce/pexpect-4.8.0-py2.py3-none-any.whl")
    version("4.7.0", sha256="2094eefdfcf37a1fdbfb9aa090862c1a4878e5c7e0e7e7088bdb511c558e5cd1", url="https://pypi.org/packages/0e/3e/377007e3f36ec42f1b84ec322ee12141a9e10d808312e5738f52f80a232c/pexpect-4.7.0-py2.py3-none-any.whl")
    version("4.6.0", sha256="3fbd41d4caf27fa4a377bfd16fef87271099463e6fa73e92a52f92dfee5d425b", url="https://pypi.org/packages/89/e6/b5a1de8b0cc4e07ca1b305a4fcc3f9806025c1b651ea302646341222f88b/pexpect-4.6.0-py2.py3-none-any.whl")
    version("4.2.1", sha256="f853b52afaf3b064d29854771e2db509ef80392509bde2dd7a6ecf2dfc3f0018", url="https://pypi.org/packages/5b/16/4859a0376be8b87bf3920b1f6e63b8a3c0ee42488babee07c87ca9316e03/pexpect-4.2.1-py2.py3-none-any.whl")
    version("3.3", sha256="dfea618d43e83cfff21504f18f98019ba520f330e4142e5185ef7c73527de5ba", url="https://pypi.org/packages/52/97/13924c85a4b7544a4174781360e0530a7fff23e62d76da0e211369dd61f5/pexpect-3.3.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-ptyprocess@0.5:", when="@4.1,4.2.1:")
    # END DEPENDENCIES

