##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyImageioFfmpeg(PythonPackage):
    version("0.4.5", sha256="db4d318f640419037a0df29bb11b1022f2f8094c90b4aac8affc7177b8ce4641", url="https://pypi.org/packages/21/00/6b345e38262894593713a9dc54dd4750209a0f75e469745509fe91fc8b63/imageio_ffmpeg-0.4.5-py3-none-manylinux2014_aarch64.whl")
    version("0.4.3", sha256="3b00bb04e8649f60d5ede91aa47b754283d1fa9fd8d40803d9871c8afd72cd50", url="https://pypi.org/packages/43/61/671bb6ec6be09cb4a10a38a65fdf362a9b8a0abf7d82aa9312a75c7e0906/imageio_ffmpeg-0.4.3-py3-none-win32.whl")


