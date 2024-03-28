# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBackportsZoneinfo(PythonPackage):
    # BEGIN VERSIONS
    version("0.2.1", sha256="fadbfe37f74051d024037f223b8e001611eac868b5c5b06144ef4d8b799862f2", url="https://pypi.org/packages/ad/85/475e514c3140937cf435954f78dedea1861aeab7662d11de232bdaa90655/backports.zoneinfo-0.2.1.tar.gz")
    version("0.2.0", sha256="23b39f0a0ab4a640091ec7c20846e7d90bda98f88e6117e5f417c2b0a5564590", url="https://pypi.org/packages/cb/c0/158dd4a82e43b0216f8fb050b6779726294302d79e9d56ff6b6588d07022/backports.zoneinfo-0.2.0.tar.gz")
    version("0.1.0", sha256="9469dfb476b6b7af51980ece42a6671bdbf2a6e08a8fd947f83a19eb24765621", url="https://pypi.org/packages/52/2b/9f93e4b8f20e9a1a2c8b6d33adbd961be534f83e874056c83dfa8cc9223b/backports.zoneinfo-0.1.0.tar.gz")
    version("0.1.0-beta1", sha256="aca81b6bca379f5764c117598ac11d894f7ca1977749375e178763bbbb30e765", url="https://pypi.org/packages/52/2d/4c6a9436cb38c1812bf1d75afb4d395ffbb3fbfba9cd8898704dc88b7e39/backports.zoneinfo-0.1.0b1.tar.gz")
    version("0.1.0-beta0", sha256="3f9f771b601a31e86233851acc2989bd14b3b57791f1d985b369f73cb0e15608", url="https://pypi.org/packages/bb/8d/b5e3e2da72f7fa687643766d52cfebdab3402bc165a25247f97a9bfba04b/backports.zoneinfo-0.1.0b0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("tzdata", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-tzdata", when="+tzdata")
    # END DEPENDENCIES

