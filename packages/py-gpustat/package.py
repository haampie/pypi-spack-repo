##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGpustat(PythonPackage):
    version("1.0.0-beta1", sha256="a25c460c5751180265814f457249ba5100baf7a055b23ad762a4e3ab3f6496dd", url="https://pypi.org/packages/09/93/53c9a9b688fc5f87ee1b2c0ad0ca4e56108b0ae31f1327e671a3f42b9eba/gpustat-1.0.0b1.tar.gz")
    version("0.6.0", sha256="f69135080b2668b662822633312c2180002c10111597af9631bb02e042755b6c", url="https://pypi.org/packages/b4/69/d8c849715171aeabd61af7da080fdc60948b5a396d2422f1f4672e43d008/gpustat-0.6.0.tar.gz")


