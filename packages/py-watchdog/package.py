# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyWatchdog(PythonPackage):
    # BEGIN VERSIONS
    version("2.1.6", sha256="a36e75df6c767cbf46f61a91c70b3ba71811dfa0aca4a324d9407a06a8b7a2e7", url="https://pypi.org/packages/e8/a8/fc4edd7d768361b00ea850e5310211d157df6b5a1db6148dd434e787d898/watchdog-2.1.6.tar.gz")
    version("0.10.3", sha256="4214e1379d128b0588021880ccaf40317ee156d4603ac388b9adcf29165e0c04", url="https://pypi.org/packages/0e/06/121302598a4fc01aca942d937f4a2c33430b7181137b35758913a8db10ad/watchdog-0.10.3.tar.gz")
    version("0.10.2", sha256="c560efb643faed5ef28784b2245cf8874f939569717a4a12826a173ac644456b", url="https://pypi.org/packages/73/c3/ed6d992006837e011baca89476a4bbffb0a91602432f73bd4473816c76e2/watchdog-0.10.2.tar.gz")
    version("0.10.1", sha256="d64786787b14c8c6a71a8cc014056776ba6b52e85d1164ef2ab50aec02723a3d", url="https://pypi.org/packages/34/65/dca6d9653656630169e9f71fe3fcf2a487b671a096cf11dc3011c822a408/watchdog-0.10.1.tar.gz")
    version("0.10.0", sha256="8e800496cdfb921cfdc62b58a11966d0d2203a35dc005b4b5b8e1ab3097b2eb5", url="https://pypi.org/packages/01/01/cc9b2fd111e19687dd42155f066718bccb414c8a728eb7df0b229742caf7/watchdog-0.10.0.tar.gz")
    version("0.9.0", sha256="965f658d0732de3188211932aeb0bb457587f04f63ab4c1e33eab878e9de961d", url="https://pypi.org/packages/bb/e3/5a55d48a29300160779f0a0d2776d17c1b762a2039b36de528b093b87d5b/watchdog-0.9.0.tar.gz")
    version("0.8.3", sha256="7e65882adb7746039b6f3876ee174952f8eaaa34491ba34333ddf1fe35de4162", url="https://pypi.org/packages/54/7d/c7c0ad1e32b9f132075967fc353a244eb2b375a3d2f5b0ce612fd96e107e/watchdog-0.8.3.tar.gz")
    version("0.8.2", sha256="33a9ab3ce2e6b1aca4d2a50752231668d69bdba4ab096d9742195ccfbef1e023", url="https://pypi.org/packages/9e/1f/bd5c41dc7e549fd7d2431518172dbf0332f203baed08feda86710f37b99a/watchdog-0.8.2.tar.gz")
    version("0.8.1", sha256="d6ec6be582b244834a888c8ccc2d451816184ab104b5454b5e5cd7649e8f671c", url="https://pypi.org/packages/96/c3/f48841b9399ba7c7331330e18d2c144ad20b29e5721e2073428d29979401/watchdog-0.8.1.tar.gz")
    version("0.8.0", sha256="a86bb2d8b94bb4bf76fcc2ff36f741c0e511ec24c4d3a1059b47d49e377d64f5", url="https://pypi.org/packages/8a/bf/1a6fbeb5dc69d55718e3f03d19a1f285eb3629200ebbc9d4ef69367a4355/watchdog-0.8.0.tar.gz")
    version("0.7.1", sha256="54ca64fdf0a2fb23cecba6349f9587e62fd31840ae22a71898a65adb8c6b52f9", url="https://pypi.org/packages/a6/ad/57748d1625d616a9f2adeef38f27f19679712b318d39cd40466bfb15d904/watchdog-0.7.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("watchmedo", default=False, description="watchmedo")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

