# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkMetal(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="652050cf9f5627dba36b31ad134e56c49040d0dcfaf93a7026018ef17330a01e", url="https://pypi.org/packages/03/c5/2d4ac87f9ea2196f8ae1b0d31b7470db9c4fdb1c981dedf48818685e2684/pyobjc-framework-Metal-10.2.tar.gz")
    version("10.1", sha256="bde76fe5d285c9c875d411a7cf6cdd7617559eabf4fb9a588f90762a0634148c", url="https://pypi.org/packages/5b/d7/c63fb8e7e5f055ebdbc1c56e93395e96d961fb708ef9321376e2ae5bafde/pyobjc-framework-Metal-10.1.tar.gz")
    version("10.0", sha256="2e50b1fc34b11654a0ecb0d6ea98f691dc5794c53e18cb70f71d6460f68dbbf3", url="https://pypi.org/packages/00/da/9da6adc32af4a548e0746c254c5165139cbd295e38f53dd321e5256641d9/pyobjc-framework-Metal-10.0.tar.gz")
    version("9.2", sha256="f483c331e07b587ef6477c79ae15a309297afa9a08c07ad9fafc4be82467d008", url="https://pypi.org/packages/52/3c/5c797a8c6ea99815d87231a710a688ab87801aaceabffd7128882c9b22e3/pyobjc-framework-Metal-9.2.tar.gz")
    version("9.1.1", sha256="d05b6caddeb4859b5560eaf006601a1e17b33fc83f4e773e94111b3c352f3531", url="https://pypi.org/packages/6d/0d/0254046dde780a32c513297beefa128e9715485cf405e2af3ef2c0436321/pyobjc-framework-Metal-9.1.1.tar.gz")
    version("9.1", sha256="0ece32a6d62b1f0f0df36af5b881ba43f73121f553ba8ab6c3b7c0f9da469d33", url="https://pypi.org/packages/c1/d0/4f93150c3652f0e3e7bf35a79884886782ae43de99eb9ade6fee627f9a7b/pyobjc-framework-Metal-9.1.tar.gz")
    version("9.0.1", sha256="18ab8fb1ce2255b3527c2a0f3dee34739f5c4a0c9c11b4dcb7336d66a19c230c", url="https://pypi.org/packages/75/c6/d758768d79eb134d11f75bd4d1e893359fe9d1339a2ebbce70362744cf82/pyobjc-framework-Metal-9.0.1.tar.gz")
    version("9.0", sha256="81c21a09f7b869316215d223ab66f38a779b5f96159f29b807d7ed18e72d4ea9", url="https://pypi.org/packages/32/a0/8c0ea1309c179c9bb1bcf84715df11c282c43297ea26407d46cfd0832ce4/pyobjc-framework-Metal-9.0.tar.gz")
    version("8.5.1", sha256="86e23f6acd14da22f4f7c747cca674d69494822ab27dba4bace86135f525afd7", url="https://pypi.org/packages/25/c7/eef8dd1b14fb69c45c96d202b63b22070674454de7944971945576d2dd43/pyobjc-framework-Metal-8.5.1.tar.gz")
    version("8.5", sha256="da7e20987ee087a6e7bf213305449b5b7345c8c55f3506b9e26a1b05215da679", url="https://pypi.org/packages/11/db/a1d113239b05ed8536c16d8158b1382e65b38e7eaf1267f14979e1e81574/pyobjc-framework-Metal-8.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
    # END DEPENDENCIES

