# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMlDtypes(PythonPackage):
    # BEGIN VERSIONS
    version("0.4.0-beta1", sha256="52e51a8db3547e763cb42411703efa418849a6c4b4caed0a6bda86e3325ae7a3", url="https://pypi.org/packages/be/32/fe988b206479617900212ee87895104bddc1e4d30d51d75db20b6c9b0a0b/ml_dtypes-0.4.0b1.tar.gz")
    version("0.3.2", sha256="533059bc5f1764fac071ef54598db358c167c51a718f68f5bb55e3dee79d2967", url="https://pypi.org/packages/39/7d/8d85fcba868758b3a546e6914e727abd8f29ea6918079f816975c9eecd63/ml_dtypes-0.3.2.tar.gz")
    version("0.3.1", sha256="60778f99194b4c4f36ba42da200b35ef851ce4d4af698aaf70f5b91fe70fc611", url="https://pypi.org/packages/16/6e/9a7a51ee1ca24b8e92109128260c5aec8340c8fe5572e9ceecddae559abe/ml_dtypes-0.3.1.tar.gz")
    version("0.3.0", sha256="c4a7f2ea1d17f8a0caee4c99ccfb8814713ba620dea1cc8ab4f478df250dba25", url="https://pypi.org/packages/ff/2c/6ceba6ee9b60e4743ddc22c87f569b94925ed2a7ce9fe62a5698958e3d14/ml_dtypes-0.3.0.tar.gz")
    version("0.2.0", sha256="6488eb642acaaf08d8020f6de0a38acee7ac324c1e6e92ee0c0fea42422cb797", url="https://pypi.org/packages/fa/47/09ca9556bf99cfe7ddf129a3423642bd482a27a717bf115090493fa42429/ml_dtypes-0.2.0.tar.gz")
    version("0.1.0", sha256="c1fc0afe63ce99069f9d7e0693a61cfd0aea90241fc3821af9953d0c11f4048a", url="https://pypi.org/packages/e8/7e/355b8db0651a2fe74437b578db1afc965b88bedd2116a83308bd7b91af43/ml_dtypes-0.1.0.tar.gz")
    version("0.0.4", sha256="45623c738d477d7a0f3f8e4c94998dc49025202c520e62e27f0ef688db2f696f", url="https://pypi.org/packages/dd/a2/5f274542c5fa4a50fa1d423927e7d3bd3e5b5777cc920a7104d1114382d9/ml_dtypes-0.0.4.tar.gz")
    version("0.0.3", sha256="d19cde6fb503b7258e8edeb895fa66b99bf9fcb6fcffb4becfae71d4890016c7", url="https://pypi.org/packages/93/7f/8ec8350c29deddce0aec64943c67fb632c579268e8aea79df7b6684a2e3a/ml_dtypes-0.0.3.tar.gz")
    version("0.0.2", sha256="14a0795ba84095dd012c2f7c387fdf813301c1e6be51e4c9b56809ee542f9520", url="https://pypi.org/packages/f6/d9/9b106fd8768c644fd0e54408fd2aab168a164cf6356817d5770589c47e06/ml_dtypes-0.0.2.tar.gz")
    version("0.0.1", sha256="49e032deeef506df0d4471955bd616a3101150cf98752d295d877bd1cb533a3a", url="https://pypi.org/packages/3d/db/791c5f863b1972a5a009f5ecda757b69200acefc8dbd813e4b37b3a10e09/ml_dtypes-0.0.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.3:")
    # END DEPENDENCIES

