# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRadicalPilot(PythonPackage):
    # BEGIN VERSIONS
    version("1.47.0", sha256="58f41a0c42fe61381f15263a63424294732606ab7cee717540c0b730308f7908", url="https://pypi.org/packages/91/8b/eefffbbf6696e34334744e9074c81cb6e16a5ed5365df082bad6f2094cf7/radical.pilot-1.47.0.tar.gz")
    version("1.39.0", sha256="7ba0bfa3258b861db71e73d52f0915bfb8b3ac1099badacf69628307cab3b913", url="https://pypi.org/packages/39/38/1f865240477134b83b9bd645749dac42d81cab49ac31be1d0be33381f445/radical.pilot-1.39.0.tar.gz")
    version("1.20.0", sha256="a0747e573a01a856dc330797dbee158f7e1cf8652001dc26f06a1d6c5e553bc6", url="https://pypi.org/packages/74/90/fbd7f43a7ea406325a8c46afa7ce98fe54ed1b41fab5f887b410fe674efb/radical.pilot-1.20.0.tar.gz")
    version("1.18.1", sha256="fd6a0ffaa727b6b9bab35d8f2dc300bf4d9c4ff3541136d83560aa7b853d6100", url="https://pypi.org/packages/bc/06/7c414e003562a139de76a2facebca9b05aa26f8b74993e09957b77a6eb69/radical.pilot-1.18.1.tar.gz")
    version("1.17.0", sha256="0bfbb321a623a684e6694241aa3b7804208846515d23afa3b930553274f4a69f", url="https://pypi.org/packages/f1/62/ce87fb7c97dccda9106bc31d5a2efe644fbdffc92eb944ab6a43b0215013/radical.pilot-1.17.0.tar.gz")
    version("1.16.0", sha256="057941a206ee96b62b97a63a507c1136b7fe821ae9f9e5eebe7949a3f53941f9", url="https://pypi.org/packages/96/96/bd5b4f929d68a1a9592377a5ec019d6caa09dbacada1aba0868714b767c8/radical.pilot-1.16.0.tar.gz")
    version("1.15.1", sha256="35c3b179a0bc85f52d2165e98e19acf2bf79037dd14f4d9ff3fc55ae0122d17e", url="https://pypi.org/packages/03/7a/8fab2f76bce69a649e1b57705240fec8fecdab65bbca05869ee9f060b870/radical.pilot-1.15.1.tar.gz")
    version("1.14.0", sha256="462471065de25f6d6e8baee705790828444c2eebb2073f5faf67a8da800d15a9", url="https://pypi.org/packages/cb/d6/3f5887b1c4e40d7279e4bc2cdd76bb6a83239990cfdeb78d40fd1f297bcb/radical.pilot-1.14.0.tar.gz")
    version("1.13.0", sha256="5bd9eef1884ccca09c242ab6d1361588a442d9cd980613c66604ba140786bde5", url="https://pypi.org/packages/60/0a/b9c8aa4eafffe8a63e5527d07a7cdb52824f0fe7cdb5f4696fa61f5c4472/radical.pilot-1.13.0.tar.gz")
    version("1.12.0", sha256="a266355d30d838f20b6cac190ce589ca919acd41883ad06aec62386239475133", url="https://pypi.org/packages/f0/66/24737d95399578bb75c95aa83db5cff7baebc784f53076102a4c1968132f/radical.pilot-1.12.0.tar.gz")
    version("1.11.2", sha256="9d239f747589b8ae5d6faaea90ea5304b6f230a1edfd8d4efb440bc3799c8a9d", url="https://pypi.org/packages/e2/aa/ecc02448425972ee727ac173d0f2fc81116fb94cb25181dbf27b26d17af5/radical.pilot-1.11.2.tar.gz")
    version("1.10.2", sha256="56e9d8b1ce7ed05eff471d7df660e4940f485027e5f353aa36fd17425846a499", url="https://pypi.org/packages/ce/b6/1678d6a77aca5b12d7d864e87fea6e315a52c6bc86f5651115b2573b63b4/radical.pilot-1.10.2.tar.gz")
    version("1.10.1", sha256="003f4c519b991bded31693026b69dd51547a5a69a5f94355dc8beff766524b3c", url="https://pypi.org/packages/38/06/7b82ef696e61b3a2c1897b3c5d4bb1f31a5714be12aa9cde2b60765d8719/radical.pilot-1.10.1.tar.gz")
    version("1.9.2", sha256="7c872ac9103a2aed0c5cd46057048a182f672191e194e0fd42794b0012e6e947", url="https://pypi.org/packages/40/26/f7f501f7fba04c9d801b429736b04dcf8fe30e907caf6f1ff0bb543bf31b/radical.pilot-1.9.2.tar.gz")
    version("1.8.0", sha256="a4c3bca163db61206e15a2d820d9a64e888da5c72672448ae975c26768130b9d", url="https://pypi.org/packages/a2/d0/5bb623b306c09383a89b67dafbdd20eac524ae21ede4b3209cbac9bf874e/radical.pilot-1.8.0.tar.gz")
    version("1.6.8", sha256="fa8fd3f348a68b54ee8338d5c5cf1a3d99c10c0b6da804424a839239ee0d313d", url="https://pypi.org/packages/d2/cd/51fce5e7bfeb775ea4638d7a7d0ff0c6d4abbca529057e9873b255072d4f/radical.pilot-1.6.8.tar.gz")
    version("1.6.7", sha256="6ca0a3bd3cda65034fa756f37fa05681d5a43441c1605408a58364f89c627970", url="https://pypi.org/packages/48/64/d5829d2adaeb668193b88098f0fee2ccf5e8e8538ef5f8a11521b6b304ee/radical.pilot-1.6.7.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

