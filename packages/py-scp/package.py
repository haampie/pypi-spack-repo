# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyScp(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.13.6", sha256="5e23f22b00bdbeed83a982c6b2dfae98c125b80019c15fbb16dd64dfd864a452", url="https://pypi.org/packages/71/cf/7f011df117ba66f20e8fe3acebac83170c5e43edfc7073cb9959b46e921a/scp-0.13.6-py2.py3-none-any.whl")
    version("0.13.5", sha256="be62d3ca534790dbaa509634fe28af6729f0d798388eaa5fdd3a1b191556dbde", url="https://pypi.org/packages/56/5e/a872b3659a651607d3f399e569b0fc581adbac892a89503f492a3277a8ab/scp-0.13.5-py2.py3-none-any.whl")
    version("0.13.4", sha256="cab0fc23407fced438565497ab092b7c20df261a9fd0975d0e6c1edad8a92cff", url="https://pypi.org/packages/22/40/ffab6a0ee521f3bbbbca0b0969fcacc90a051a2a73fbf73d103e66458d37/scp-0.13.4-py2.py3-none-any.whl")
    version("0.13.3", sha256="f2fa9fb269ead0f09b4e2ceb47621beb7000c135f272f6b70d3d9d29928d7bf0", url="https://pypi.org/packages/b7/37/122d300034f2c8576158a7830e02c687730635e65a95f9eb2b4eb002554d/scp-0.13.3-py2.py3-none-any.whl")
    version("0.13.2", sha256="26c0bbc7ea29c30ec096ae67b0afa7a6b7c557b2ce8f740109ee72a0d52af7d1", url="https://pypi.org/packages/4d/7a/3d76dc5ad8deea79642f50a572e1c057cb27e8b427f83781a2c05ce4e5b6/scp-0.13.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-paramiko", when="@0.12.1:0.12,0.13.3:")
    # END DEPENDENCIES

