##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPydeface(PythonPackage):
    version("2.0.2", sha256="beb838c4246b8c5798fdc3a331f3064d4aac1bcd1ac9c26b991c9f28207d059e", url="https://pypi.org/packages/81/78/257fe9f0715883bbecc2a68e3d965272956c292d0981d717665da69f4efd/pydeface-2.0.2-py3-none-any.whl")
    version("2.0.0", sha256="e25edae9525c1a870741c8aa84aea6ec6a811b8ef6898df823fa9816bdaf1327", url="https://pypi.org/packages/07/88/518e90d8ec957c5dd3e2963dede50ba97e551123cb0dbb51cf26fb29e6c2/pydeface-2.0.0.tar.gz")
    version("1.0", sha256="e5a9a56e658ed99a3b14eaa69db6eb76b6adc7ee54a3f19d6bf3f7f574aa35e7", url="https://pypi.org/packages/69/2b/83a01eb83bf12f3312edf35c990ae0bb595ae2a180bef186f38d6e854233/pydeface-1.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-nibabel", when="@2.0.2:")
        depends_on("py-nipype", when="@2.0.2:")
        depends_on("py-numpy", when="@2.0.2:")
        depends_on("py-setuptools", when="@2.0.2:")

