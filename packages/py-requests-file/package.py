##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRequestsFile(PythonPackage):
    version("2.0.0", sha256="3e493d390adb44aa102ebea827a48717336d5268968c370eaf19abaf5cae13bf", url="https://pypi.org/packages/10/fd/321e33597e09cb4368d361b0b6c6573ef45d5f693acef41ba33673a55b7c/requests_file-2.0.0-py2.py3-none-any.whl")
    version("1.5.1", sha256="dfe5dae75c12481f68ba353183c53a65e6044c923e64c24b2209f6c7570ca953", url="https://pypi.org/packages/77/86/cdb5e8eaed90796aa83a6d9f75cfbd37af553c47a291cd47bc410ef9bdb2/requests_file-1.5.1-py2.py3-none-any.whl")
    version("1.5.0", sha256="92d5a65342742962208e63cfa384c6559f9180c187a866609ff34d2172a7f86f", url="https://pypi.org/packages/95/59/cdc5a26669e769abbf6812298970adf8ac7c749c20c60ec779d27bc15d59/requests_file-1.5.0-py2.py3-none-any.whl")
    version("1.4.3", sha256="8f04aa6201bacda0567e7ac7f677f1499b0fc76b22140c54bc06edf1ba92e2fa", url="https://pypi.org/packages/a0/f9/8c1712aea1b70c6a77db322bb18610a078ba8f44876e95289137953db30d/requests-file-1.4.3.tar.gz")
    version("1.4.2", sha256="f518e7cfe048e053fd1019dfb891b4c55b871c56c5a31693d733240c80b8f191", url="https://pypi.org/packages/a6/8e/acc2d49a16014eaf3ac4f8699c2d4141169cefdb442da131cce7934a36d9/requests-file-1.4.2.tar.gz")
    version("1.4.1", sha256="d75823cccd271caa7303304f9f7d44e12db9f77d844491c5ec9bd44af0844ebc", url="https://pypi.org/packages/d4/6a/3503eaf7b8c8b85fc07485234d914fd264b5e81bbb0c6bdf591ccb09972b/requests-file-1.4.1.tar.gz")
    version("1.4", sha256="d6912b19971d3f11a5f258640705cedc7df9eb5a3b9d58c9ce3367b4a9261bc8", url="https://pypi.org/packages/ff/1f/11aa5c35218501935e8e05e4ae52f72f416eeb69a9e8fe84e5ef660ccffb/requests-file-1.4.tar.gz")

    with default_args(type="run"):
        depends_on("py-requests@1:", when="@1.5:")
        depends_on("py-six", when="@1.5:1")

