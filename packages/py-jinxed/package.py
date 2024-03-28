# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJinxed(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.2.1", sha256="37422659c4925969c66148c5e64979f553386a4226b9484d910d3094ced37d30", url="https://pypi.org/packages/d8/96/f79f67f5f3c2d24bb8183a1d5bbf0ef4f39e343d49a46203e4d7a51ee849/jinxed-1.2.1-py2.py3-none-any.whl")
    version("1.2.0", sha256="cfc2b2e4e3b4326954d546ba6d6b9a7a796ddcb0aef8d03161d005177eb0d48b", url="https://pypi.org/packages/23/22/9b3481b11f32aedf1cc403f290b92bd23327d04e359808482a69b2bc3665/jinxed-1.2.0-py2.py3-none-any.whl")
    version("1.1.0", sha256="6a61ccf963c16aa885304f27e6e5693783676897cea0c7f223270c8b8e78baf8", url="https://pypi.org/packages/81/c0/ef7c7ddcf23b82010bbdbc639e6eae92ecf2b73277aa69df5fbf6b850d82/jinxed-1.1.0-py2.py3-none-any.whl")
    version("1.0.1", sha256="602f2cb3523c1045456f7b6d79ac19297fd8e933ae3bd9159845dc857f2d519c", url="https://pypi.org/packages/c9/d5/6413973268e2b74af6b687c5e56fa1aabc5e7ebc412fe3803a21f5ba4cc0/jinxed-1.0.1-py2.py3-none-any.whl")
    version("1.0.0", sha256="79ceb7097ba9d905000905173554092e81fe31aebb107b9566a15767dfdc3a82", url="https://pypi.org/packages/22/a8/6e3bcc6e6f90d5abb5c618d5142cc7cc8fb2a66fa9af9928ca3f2a03f96b/jinxed-1.0.0-py2.py3-none-any.whl")
    version("0.5.6", sha256="5d34c4537c5469f029aabb4fe6a5a10f5efeb7b6ce771655925daf85ee6a3221", url="https://pypi.org/packages/c4/42/4fc34a6c965c717453e71b37d1add8b6af9ecd20ff3fd14a6eca3e821bba/jinxed-0.5.6-py2.py3-none-any.whl")
    version("0.5.5", sha256="1a15493d93f1f477d504c30c3f1fb7806ea7a415f8e031278b2bda54aada7d36", url="https://pypi.org/packages/c1/3c/0f3e82f639c4515af742bfe5c36b4d7a79507e70c24d0414571fecbce620/jinxed-0.5.5-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-ansicon", when="@0.5.6: platform=windows")
    # END DEPENDENCIES

