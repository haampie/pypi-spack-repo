# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRequestsFile(PythonPackage):
    # BEGIN VERSIONS
    version("2.0.0", sha256="3e493d390adb44aa102ebea827a48717336d5268968c370eaf19abaf5cae13bf", url="https://pypi.org/packages/10/fd/321e33597e09cb4368d361b0b6c6573ef45d5f693acef41ba33673a55b7c/requests_file-2.0.0-py2.py3-none-any.whl")
    version("1.5.1", sha256="dfe5dae75c12481f68ba353183c53a65e6044c923e64c24b2209f6c7570ca953", url="https://pypi.org/packages/77/86/cdb5e8eaed90796aa83a6d9f75cfbd37af553c47a291cd47bc410ef9bdb2/requests_file-1.5.1-py2.py3-none-any.whl")
    version("1.5.0", sha256="92d5a65342742962208e63cfa384c6559f9180c187a866609ff34d2172a7f86f", url="https://pypi.org/packages/95/59/cdc5a26669e769abbf6812298970adf8ac7c749c20c60ec779d27bc15d59/requests_file-1.5.0-py2.py3-none-any.whl")
    version("1.4.3", sha256="75c175eed739270aec3c5279ffd74e6527dada275c5c0d76b5817e9c86bb7dea", url="https://pypi.org/packages/23/9c/6e63c23c39e53d3df41c77a3d05a49a42c4e1383a6d2a5e3233161b89dbf/requests_file-1.4.3-py2.py3-none-any.whl")
    version("1.4.2", sha256="f518e7cfe048e053fd1019dfb891b4c55b871c56c5a31693d733240c80b8f191", url="https://pypi.org/packages/a6/8e/acc2d49a16014eaf3ac4f8699c2d4141169cefdb442da131cce7934a36d9/requests-file-1.4.2.tar.gz")
    version("1.4.1", sha256="8b3927545f8ccd424fce30ca5987a0561db1598f811f7bdff124c24b33a057cf", url="https://pypi.org/packages/ab/5b/203b875c232c74868306b0aa2d8b8f9c94c58a6fd1e293a1eda33d332323/requests_file-1.4.1-py2.py3-none-any.whl")
    version("1.4", sha256="d6912b19971d3f11a5f258640705cedc7df9eb5a3b9d58c9ce3367b4a9261bc8", url="https://pypi.org/packages/ff/1f/11aa5c35218501935e8e05e4ae52f72f416eeb69a9e8fe84e5ef660ccffb/requests-file-1.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-requests@1:", when="@1.5:")
        depends_on("py-six", when="@1.5:1")
    # END DEPENDENCIES

