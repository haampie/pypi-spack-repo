##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDotnetcore2(PythonPackage):
    version("2.1.23", sha256="76c9dea3ebeecfd1485e7f275072c694e856e707527b34af3fdf5f4f8f8f6461", url="https://pypi.org/packages/00/b8/2245464ff1718a8e80f79fd294ad38847d9ef80fbd6ef27ca5d6e922d86e/dotnetcore2-2.1.23-py3-none-manylinux1_x86_64.whl")
    version("2.1.22", sha256="8c2d1734a4dc5e3da69c9ee0329c7b5881061bd24cc853d82b35cef4caacc879", url="https://pypi.org/packages/54/b8/fd6b3d47c3e41691d9dc04df956f44bd9b70bb0c8734151426438c3c0b9d/dotnetcore2-2.1.22-py3-none-manylinux1_x86_64.whl")
    version("2.1.21", sha256="0c778dae43342f477d2a954c0feea174e9dac6882eced236cfc88338baec5074", url="https://pypi.org/packages/42/8b/67c8a4cd6aaa31cbfcdeb79880087d4ddedc06bf11c1d8505ab4af3f18e1/dotnetcore2-2.1.21-py3-none-win32.whl")
    version("2.1.20", sha256="80b776671cc766e07f9f7425aa92c3f81c2149187b478a3262f1be77d3e8ba79", url="https://pypi.org/packages/92/fe/1d86a30a961c4705f8815199f3f0c82400e8975db7d4697994dc56139b1e/dotnetcore2-2.1.20-py3-none-win32.whl")
    version("2.1.19", sha256="e5a7280fbcdb8e3b4b4ce8e73930e10d0436102d124087b6972d014d057e56d7", url="https://pypi.org/packages/a7/bd/a79a6ee05963f0d81b45378d054ba673e7e3e150098824821f60dddd9e77/dotnetcore2-2.1.19-py3-none-manylinux1_x86_64.whl")
    version("2.1.18", sha256="6b22b6999dfa9b646b6df04cfe27507100e42521bfee06889326d58ee50bf98a", url="https://pypi.org/packages/b7/60/7486423fc7ac46966435a829a9b40f6de73462d35efa4b10ed143b9860e1/dotnetcore2-2.1.18-py3-none-manylinux1_x86_64.whl")
    version("2.1.17", sha256="4f61cb6885b19ca1e6a74e1f9ee5539c993be5f5dcb320530b6537e541d3bc9f", url="https://pypi.org/packages/61/ee/0e1a27dec380600dca284a27d26a1e16d2e3a64b81d9c152b36eb018990d/dotnetcore2-2.1.17-py3-none-win32.whl")
    version("2.1.16", sha256="e017d171bb3f94168945f1af8afdcc2533afd12fc63bd6bbb10dfe9cf1d783f8", url="https://pypi.org/packages/f0/a3/c326bf11c676d305e6a13cf87c04c6a500d3de6e468173f678fba373020f/dotnetcore2-2.1.16-py3-none-manylinux1_x86_64.whl")
    version("2.1.15", sha256="0eebeccf3185845ba4337714278e0eb3a1e3719ed3fba4c472e33e442e0455c6", url="https://pypi.org/packages/6c/8b/9d0767ed220f636d4f56479255cbe22103bfe2360c4bd8bbefaa449ef73d/dotnetcore2-2.1.15-py3-none-win32.whl")
    version("2.1.14", sha256="693f9a0c021a5d8176c34ae7bfc78ba9c7c88023332674587282cddd3580a444", url="https://pypi.org/packages/59/a1/e6500aca9dbb476858561e24d7f5f516db09ead0057fe992ebb041e7e995/dotnetcore2-2.1.14-py3-none-win32.whl")

    with default_args(type="run"):
        depends_on("py-distro@1.2:", when="@2.1.5:")

