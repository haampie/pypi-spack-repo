##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyWatchdog(PythonPackage):
    version("4.0.0", sha256="e3e7065cbdabe6183ab82199d7a4f6b3ba0a438c5a512a68559846ccb76a78ec", url="https://pypi.org/packages/cd/3c/43eeaa9ea17a2657d639aa3827beaa77042809410f86fb76f0d0ea6a2102/watchdog-4.0.0.tar.gz")
    version("3.0.0", sha256="4d98a320595da7a7c5a18fc48cb633c2e73cda78f93cac2ef42d42bf609a33f9", url="https://pypi.org/packages/95/a6/d6ef450393dac5734c63c40a131f66808d2e6f59f6165ab38c98fbe4e6ec/watchdog-3.0.0.tar.gz")
    version("2.3.1", sha256="d9f9ed26ed22a9d331820a8432c3680707ea8b54121ddcc9dc7d9f2ceeb36906", url="https://pypi.org/packages/a5/17/a31fc6b90ff861a27debd0650bfbca17e074fdc3e037f392872fad76c726/watchdog-2.3.1.tar.gz")
    version("2.3.0", sha256="9d39effe6909be898ba3e7286a9e9b17a6a9f734fb1ef9dde3e9bb68715fca39", url="https://pypi.org/packages/d1/77/6451ac9c31630bab57e4dcd25e701c379547ccc0974d7d6d94b97e46ca7f/watchdog-2.3.0.tar.gz")
    version("2.2.1", sha256="cdcc23c9528601a8a293eb4369cbd14f6b4f34f07ae8769421252e9c22718b6f", url="https://pypi.org/packages/11/6f/0396d373e039b89c60e23a1a9025edc6dd203121fe0af7d1427e85d5ec98/watchdog-2.2.1.tar.gz")
    version("2.2.0", sha256="83cf8bc60d9c613b66a4c018051873d6273d9e45d040eed06d6a96241bd8ec01", url="https://pypi.org/packages/c3/fb/bd960970258366b0704307ccd12617d64201407bfb6d31ae412d2762ccf1/watchdog-2.2.0.tar.gz")
    version("2.1.9", sha256="43ce20ebb36a51f21fa376f76d1d4692452b2527ccd601950d69ed36b9e21609", url="https://pypi.org/packages/42/f7/da8e889f8626786eac9454e8d2718fc79359ed517be20cdd50c647167d39/watchdog-2.1.9.tar.gz")
    version("2.1.8", sha256="6d03149126864abd32715d4e9267d2754cede25a69052901399356ad3bc5ecff", url="https://pypi.org/packages/90/61/ddbf959d24fab35a98a8311e95d581e55109560e524f1a5a299ee991499d/watchdog-2.1.8.tar.gz")
    version("2.1.7", sha256="3fd47815353be9c44eebc94cc28fe26b2b0c5bd889dafc4a5a7cbdf924143480", url="https://pypi.org/packages/b3/d2/a04951838e0b0cea20aff5214109144e6869101818e7f90bf3b68ea2facf/watchdog-2.1.7.tar.gz")
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


