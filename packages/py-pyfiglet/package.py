##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyfiglet(PythonPackage):
    version("0.8.post1", sha256="c6c2321755d09267b438ec7b936825a4910fec696292139e664ca8670e103639", url="https://pypi.org/packages/f9/02/48293654fb2e4fdeb4d927f00a380230a832744b6c9af757373a72d018d1/pyfiglet-0.8.post1.tar.gz")
    version("0.8.post0", sha256="2994451ea67c77cd97f81f52087ccae6921d78d9402920995419893a979b5ace", url="https://pypi.org/packages/36/b6/26fdb3b054eb575cac417d7fe0061182a566e1da720c1876f7c363aa44df/pyfiglet-0.8.post0.tar.gz")
    version("0.7.6", sha256="97d59651b40da6ddf7e961157c480a7a04b48214d8c7231adc8c15e43aa5d722", url="https://pypi.org/packages/58/89/d0144fac7a28179603af2faf17e9cd4a6662c8c6da537c0adcddb1bb5c17/pyfiglet-0.7.6.tar.gz")
    version("0.7.5", sha256="446194e1fc3257ffc8024eafd3b486394847597f6210278d76bd582850205e12", url="https://pypi.org/packages/a2/65/4e29896298591d748f5ce4e96642b8a0a876b64ed7226b5ae65fae81e5c9/pyfiglet-0.7.5.tar.gz")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.0.1:")

